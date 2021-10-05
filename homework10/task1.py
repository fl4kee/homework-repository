import asyncio
import datetime
import json
import os
import time

import aiohttp
import xmltodict  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

t0 = time.time()
BASE_URL = "https://markets.businessinsider.com"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                   Chrome/94.0.4606.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\
               */*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

# dict for currencies
current_rate = {}
# list for company data
companies_data = []


def round_float(float_num):
    """Rounds incoming float to 2 digits after floating point"""
    return float(f"{float_num:.2f}")


async def get_current_rate(session, id):
    """
    function takes an id that corresponds to certaing currency
    list of ids you can find here http://www.cbr.ru/scripts/XML_val.asp?d=0
    it returns current exchange rate in rubles
    """
    current_date = datetime.datetime.now().strftime('%d.%m.%Y')
    curr_rates_url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}'
    async with session.get(url=curr_rates_url, headers=HEADERS) as response:
        response_text = await response.text()
        currencies = xmltodict.parse(response_text)
        for i in currencies['ValCurs']['Valute']:
            if i['@ID'] == id:
                current_rate['USD'] = float(i['Value'].replace(',', '.'))
                break


async def parse_details_page(session, url):
    """
    function parses details page of company
    return it s code, P/E and potential profit
    potential profit is calcilated from week_high and week_low
    if there no data for these variables potential profit cant be calculated
    """
    async with session.get(url=url, headers=HEADERS) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, 'lxml')
        code = soup.find('span', class_='price-section__category').text.strip().split()[-1]
        pe = float(soup.find('div', class_='snapshot__data-item')
                       .find(text=True).strip().replace(',', ''))
        try:
            week_high = float(soup.find('div', class_='snapshot__data-item--right')
                                  .find(text=True).strip().replace(',', ''))
        except AttributeError:
            week_high = None
        try:
            week_low = float(soup.find('div', class_='snapshot__data-item')
                                 .find(text=True).strip().replace(',', ''))
        except AttributeError:
            week_low = None
        if week_high and week_low:
            potential_profit = round_float(week_high - week_low)
        else:
            potential_profit = 'No data for calculating potential profit'
        return (code, pe, potential_profit)


async def get_page_data(session, page):
    page_url = BASE_URL + f'/index/components/s&p_500?p={str(page)}'
    # # async requests with  aiohttp
    async with session.get(url=page_url, headers=HEADERS) as response:
        response_text = await response.text()

        # # Getting data from soup object
        soup = BeautifulSoup(response_text, 'lxml')
        company_items = soup.find('tbody', class_="table__tbody").find_all("tr")
        for ci in company_items:
            company_data = ci.find_all('td')
            details_page_link = BASE_URL + company_data[0].find('a').attrs['href']

            company_name = company_data[0].find("a").text.strip()
            curr_price = round_float(float(company_data[1].text.split()[0]
                                                          .strip()
                                                          .replace(',', '')) * current_rate['USD'])
            code, pe, potential_profit = await parse_details_page(session, details_page_link)
            growth = round_float(float(company_data[-1].find("span").text.strip().replace(',', '')))

            companies_data.append(
                {
                    "code": code,
                    "name": company_name,
                    "price": curr_price,
                    "P/E": pe,

                    "growth": growth,
                    "potential-profit": potential_profit
                }
            )

    print(f"[INFO] {page} page is parsed")


async def gather_data():
    # creating session
    async with aiohttp.ClientSession() as session:

        await get_current_rate(session, 'R01235')
        # parsing pagination
        response = await session.get(url=BASE_URL + '/index/components/s&p_500', headers=HEADERS)
        soup = BeautifulSoup(await response.text(), 'lxml')
        pages_count = int(soup.find("div", class_="finando_paging margin-top--small")
                              .find_all("a")[-2].text)

        # task queue
        tasks = []

        # scrapper works for every page
        for page in range(1, pages_count + 1):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)

        await asyncio.gather(*tasks)


def most_expensv_cmpns(data):
    """filteres data by most expensive price"""
    return sorted(data, key=lambda x: x['price'], reverse=True)[0:10]


def lowest_pe(data):
    """filteres data by lowest P/E"""
    return sorted(data, key=lambda x: x['P/E'])[0:10]


def highest_growth(data):
    """filteres data by highest growth"""
    return sorted(data, key=lambda x: x['growth'], reverse=True)[0:10]


def highest_profit(data):
    """filteres data by highest potential-profit"""
    filtered_data = list(filter(lambda x: isinstance(x['potential-profit'], float), data))
    return sorted(filtered_data, key=lambda x: x['potential-profit'], reverse=True)[0:10]


def create_file(name, filter_func):
    """Creates file with filtered data"""
    with open(name, "w", encoding="utf-8") as file:
        json.dump(filter_func(companies_data), file, indent=4, ensure_ascii=False)


def main():
    # if os is windows set corresponding event loop policy
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(gather_data())
    # creating json files
    create_file('10_most_expensive_stocks.json', most_expensv_cmpns)
    create_file('10_lowest_p_e.json', lowest_pe)
    create_file('10_highest_growth.json', highest_growth)
    create_file('10_highest_profit.json', highest_profit)


if __name__ == '__main__':
    main()
    print(time.time() - t0)
