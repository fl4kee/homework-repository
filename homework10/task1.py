import asyncio
import json
import os
from datetime import datetime
from typing import Callable, List, Union

import xmltodict  # type: ignore
from aiohttp import ClientSession
from bs4 import BeautifulSoup  # type: ignore


def round_float_str(float_str):
    """Rounds incoming float to 2 digits after floating point"""
    float_num = float(float_str)
    return float(f"{float_num:.2f}")


class WebScraper:
    def __init__(self, current_date=datetime.now()):
        self.current_date = current_date.strftime('%d.%m.%Y')
        self.url = "https://markets.businessinsider.com"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/94.0.4606.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\
                    */*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        self.number_of_pages = None
        self.current_rate = None
        self.parsed_data = []
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.gather_data())

    async def get_current_rate(self, session: ClientSession, id: str) -> float:
        """
        function takes an id that corresponds to certaing currency
        list of ids you can find here http://www.cbr.ru/scripts/XML_val.asp?d=0
        it returns current exchange rate in rubles
        returns 0 if id is not found
        """
        curr_rates_url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={self.current_date}'
        async with session.get(url=curr_rates_url) as response:
            response_text = await response.text()
            currencies = xmltodict.parse(response_text)
            for i in currencies['ValCurs']['Valute']:
                if i['@ID'] == id:
                    return float(i['Value'].replace(',', '.'))
            raise AttributeError('No id is found')

    async def fetch_details_page(self,
                                 session: ClientSession,
                                 url: str) -> tuple[str, str, str]:
        """
        Takes url of details page and returns code, P\\E and potential profit in tuple
        """
        async with session.get(url) as response:
            print(url)
            response_text = await response.text()
            decoded_response_text = response_text.encode('utf-8').decode('unicode-escape')
            soup = BeautifulSoup(decoded_response_text, 'lxml')
            company_code = self.get_company_code(soup)
            company_pe = self.get_company_pe(soup)
            company_potential_profit = self.get_company_potential_profit(soup)
            return (company_code, company_pe, company_potential_profit)

    async def fetch(self, session: ClientSession, url: str) -> None:
        """
        Takes url of a page parses
        and adds all information about one company in list with parsed data
        """
        async with session.get(url) as response:
            print(url)
            response_text = await response.text()
            decoded_response_text = response_text.encode('utf-8').decode('unicode-escape')
            company_items = await self.get_company_items(decoded_response_text)
            for ci in company_items:
                company_data = ci.find_all('td')
                name = self.get_company_name(company_data)
                price = self.get_company_price(company_data)
                details_url = self.get_company_details_url(company_data)
                growth = self.get_company_growth(company_data)
                code, pe, potential_profit = await self.fetch_details_page(session, details_url)

                self.parsed_data.append({
                    "code": code,
                    "name": name,
                    "price": round_float_str(price) * self.current_rate,
                    "P/E": round_float_str(pe),
                    "growth": round_float_str(growth),
                    "potential-profit": round_float_str(potential_profit) * self.current_rate
                })

    def get_company_potential_profit(self, data: BeautifulSoup) -> str:
        """
        function parses potential profit of company
        if there is no information to parse returns coresponding message
        """
        try:
            week_high: Union[str, None] = (data.find("div", string="52 Week High")
                                               .parent
                                               .find(text=True)
                                               .strip()
                                               .replace(',', ''))
        except AttributeError:
            week_high = None
        try:
            week_low: Union[str, None] = (data.find("div", string="52 Week Low")
                                              .parent
                                              .find(text=True)
                                              .strip()
                                              .replace(',', ''))
        except AttributeError:
            week_low = None

        if week_high and week_low:
            potential_profit = str((float(week_high) - float(week_low)))
        else:
            potential_profit = 'No data for calculating potential profit'

        return potential_profit

    def get_company_growth(self, data: BeautifulSoup) -> str:
        """
        function parses potential growth of company
        if there is no information to parse returns coresponding message
        """
        try:
            return (data[-1].find("span").text.strip().replace(',', ''))
        except AttributeError:
            return 'No growth data for this company'

    def get_company_pe(self, data: BeautifulSoup) -> str:
        """
        function parses P\\E of company
        if there is no information to parse returns coresponding message
        """
        try:
            return (data.find("div", string="P/E Ratio").parent
                                                        .find(text=True)
                                                        .strip()
                                                        .replace(',', ''))
        except AttributeError:
            return 'No P/E data for this company'

    def get_company_code(self, data: BeautifulSoup) -> str:
        """
        function parses code of company
        if there is no information to parse returns coresponding message
        """
        try:
            return data.find('span', class_='price-section__category').text.strip().split()[-1]
        except AttributeError:
            return 'No code data for this company'

    def get_company_name(self, data: BeautifulSoup) -> str:
        """
        function parses name of company
        if there is no information to parse returns coresponding message
        """
        try:
            return data[0].find("a").text.strip()
        except AttributeError:
            return 'No name data for this company'

    def get_company_details_url(self, data: BeautifulSoup) -> str:
        """
        function parses url of company
        if there is no information to parse returns coresponding message
        """
        try:
            return self.url + data[0].find('a').attrs['href']
        except AttributeError:
            return 'No URL for this company'

    async def get_company_items(self, text: str) -> BeautifulSoup:
        """
        function parses all company data fro row in a table
        if there is no information to parse returns coresponding message
        """
        try:
            soup = BeautifulSoup(text, 'lxml')
            return soup.find('tbody', class_="table__tbody").find_all("tr")
        except AttributeError as e:
            return f'No companies found, {e}'

    async def get_number_of_pages(self, session: ClientSession, url: str) -> int:
        """
        function parses and returns number of pages
        """
        async with session.get(url) as response:
            text = await response.text()
            decoded_text = text.encode('utf-8').decode('unicode-escape')
            soup = BeautifulSoup(decoded_text, 'lxml')
            return int(soup.find("div", class_="finando_paging margin-top--small")
                           .find_all("a")[-2].text)

    def get_company_price(self, data: BeautifulSoup) -> str:
        """
        function parses price of company
        if there is no information to parse returns coresponding message
        """
        try:
            return (data[1].text.split()[0]
                           .strip()
                           .replace(',', ''))
        except AttributeError:
            return 'No price for this company'

    async def gather_data(self) -> None:
        """
        Creating and delegating tasks
        """
        tasks = []
        async with ClientSession(headers=self.headers) as session:
            self.current_rate = await self.get_current_rate(session, 'R01235')
            index_url = self.url + '/index/components/s&p_500'
            self.number_of_pages = await self.get_number_of_pages(session, url=index_url)

            for page in range(1, self.number_of_pages + 1):
                url = self.url + f'/index/components/s&p_500?p={str(page)}'
                task = asyncio.create_task(self.fetch(session, url))
                tasks.append(task)

            await asyncio.gather(*tasks)


class Data:
    def __init__(self, data: List) -> None:
        self.data = data

    def most_expensv_cmpns(self, data: List) -> List:
        """filteres data by most expensive price"""
        return sorted(data, key=lambda x: x['price'], reverse=True)[0:10]

    def lowest_pe(self, data: List) -> List:
        """filteres data by lowest P/E"""
        filtered_data = list(filter(lambda x: isinstance(x['P/E'], float), data))
        return sorted(filtered_data, key=lambda x: x['P/E'])[0:10]

    def highest_growth(self, data: List) -> List:
        """filteres data by highest growth"""
        return sorted(data, key=lambda x: x['growth'], reverse=True)[0:10]

    def highest_profit(self, data: List) -> List:
        """filteres data by highest potential-profit"""
        filtered_data = list(filter(lambda x: isinstance(x['potential-profit'], float), data))
        return sorted(filtered_data, key=lambda x: x['potential-profit'], reverse=True)[0:10]

    def create_file(self, name: str, filter_func: Callable) -> None:
        """Creates file with filtered data"""
        with open(name, "w", encoding="utf-8") as file:
            json.dump(filter_func(self.data), file, indent=4, ensure_ascii=False)

    def create_files(self) -> None:
        """creating files with data"""
        self.create_file('10_most_expensive_stocks_.json', self.most_expensv_cmpns)
        self.create_file('10_lowest_p_e_.json', self.lowest_pe)
        self.create_file('10_highest_growth.json', self.highest_growth)
        self.create_file('10_highest_profit.json', self.highest_profit)
