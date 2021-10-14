import asyncio
import json
import os
from datetime import datetime
from typing import Callable, List, Union

import xmltodict  # type: ignore
from aiohttp import ClientSession
from bs4 import BeautifulSoup  # type: ignore


def round_float(float_num):
    """Rounds incoming float to 2 digits after floating point"""
    return float(f"{float_num:.2f}")


class WebScraper:
    def __init__(self):
        self.url = "https://markets.businessinsider.com"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/94.0.4606.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\
                    */*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        self.number_of_pages = None
        self.current_rate = {}
        self.parsed_data = []
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.gather_data())

    async def get_current_rate(self, session: ClientSession, id: str) -> None:
        current_date = datetime.now().strftime('%d.%m.%Y')
        curr_rates_url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}'
        async with session.get(url=curr_rates_url) as response:
            print(type(session))
            response_text = await response.text()
            currencies = xmltodict.parse(response_text)
            for i in currencies['ValCurs']['Valute']:
                if i['@ID'] == id:
                    self.current_rate['USD'] = float(i['Value'].replace(',', '.'))
                    break

    async def fetch_details_page(self,
                                 session: ClientSession,
                                 url: str) -> tuple[str, Union[float, str], Union[str, float]]:

        async with session.get(url) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, 'lxml')
            company_code = await self.get_company_code(soup)
            company_pe = await self.get_company_pe(soup)
            company_potential_profit = await self.get_company_potential_profit(soup)
            return (company_code, company_pe, company_potential_profit)

    async def fetch(self, session: ClientSession, url: str) -> None:
        async with session.get(url) as response:
            response_text = await response.text()
            company_items = await self.get_company_items(response_text)
            for ci in company_items:
                company_data = ci.find_all('td')
                name = await self.get_company_name(company_data)
                price = await self.get_company_price(company_data)
                details_url = await self.get_company_details_url(company_data)
                growth = await self.get_company_growth(company_data)
                code, pe, potential_profit = await self.fetch_details_page(session, details_url)

                self.parsed_data.append({
                    "code": code,
                    "name": name,
                    "price": price,
                    "P/E": pe,
                    "growth": growth,
                    "potential-profit": potential_profit
                })

    async def get_company_potential_profit(self, data: BeautifulSoup) -> Union[str, float]:
        print(type(data))
        try:
            week_high: Union[float, None] = float(data.find("div", string="52 Week High")
                                                      .parent
                                                      .find(text=True)
                                                      .strip()
                                                      .replace(',', ''))
        except AttributeError:
            week_high = None
        try:
            week_low: Union[float, None] = float(data.find("div", string="52 Week Low")
                                                     .parent
                                                     .find(text=True)
                                                     .strip()
                                                     .replace(',', ''))
        except AttributeError:
            week_low = None

        if week_high and week_low:
            potential_profit = round_float((week_high - week_low) * self.current_rate['USD'])
        else:
            potential_profit = 'No data for calculating potential profit'

        return potential_profit

    async def get_company_growth(self, data: BeautifulSoup) -> Union[float, str]:
        try:
            return round_float(float(data[-1].find("span").text.strip().replace(',', '')))
        except AttributeError:
            return 'No growth data for this company'

    async def get_company_pe(self, data: BeautifulSoup) -> Union[float, str]:
        try:
            return round_float(float(data.find("div", string="P/E Ratio").parent
                                                                         .find(text=True)
                                                                         .strip()
                                                                         .replace(',', '')))
        except AttributeError:
            return 'No P/E data for this company'

    async def get_company_code(self, data: BeautifulSoup) -> str:
        try:
            return data.find('span', class_='price-section__category').text.strip().split()[-1]
        except AttributeError:
            return 'No code data for this company'

    async def get_company_name(self, data: BeautifulSoup) -> str:
        try:
            return data[0].find("a").text.strip()
        except AttributeError:
            return 'No name data for this company'

    async def get_company_details_url(self, data: BeautifulSoup) -> str:
        try:
            return self.url + data[0].find('a').attrs['href']
        except AttributeError:
            return 'No URL for this company'

    async def get_company_items(self, text: str) -> BeautifulSoup:
        try:
            soup = BeautifulSoup(text, 'lxml')
            return soup.find('tbody', class_="table__tbody").find_all("tr")
        except AttributeError as e:
            return f'No companies found, {e}'

    async def get_number_of_pages(self, session: ClientSession, url: str) -> int:
        async with session.get(url) as response:
            text = await response.text()
            soup = BeautifulSoup(text, 'lxml')
            return int(soup.find("div", class_="finando_paging margin-top--small")
                           .find_all("a")[-2].text)

    async def get_company_price(self, data: BeautifulSoup) -> Union[float, str]:
        try:
            return round_float(float(data[1].text.split()[0]
                                            .strip()
                                            .replace(',', '')) * self.current_rate['USD'])
        except AttributeError:
            return 'No price for this company'

    async def gather_data(self) -> None:
        tasks = []
        async with ClientSession(headers=self.headers) as session:
            await self.get_current_rate(session, 'R01235')
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
        self.create_file('10_most_expensive_stocks_.json', self.most_expensv_cmpns)
        self.create_file('10_lowest_p_e_.json', self.lowest_pe)
        self.create_file('10_highest_growth.json', self.highest_growth)
        self.create_file('10_highest_profit.json', self.highest_profit)
