import os
from datetime import datetime

import pytest
from aioresponses import aioresponses  # type: ignore

from homework10.task1 import Data, WebScraper

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                   Chrome/94.0.4606.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\
               */*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Charset': 'utf-8'
}
current_date = datetime(2021, 9, 10, 17, 5, 55)


def read_file(file):
    with open(file, 'r') as f:
        return ''.join(f.readlines())


def read_json(file):
    with open(file, 'r') as f:
        return f.readlines()


fake_index_html = read_file(os.path.join(os.path.dirname(__file__),
                            'test_index_page.html'))
fake_abt_html = read_file(os.path.join(os.path.dirname(__file__),
                          'abt-stock.html'))
fake_aos_html = read_file(os.path.join(os.path.dirname(__file__),
                          'aos-stock.html'))
fake_mmm_html = read_file(os.path.join(os.path.dirname(__file__),
                          'mmm-stock.html'))
test_10_highest_growth = read_json(os.path.join(os.path.dirname(__file__),
                                   '10_highest_growth_test.json'))
test_10_highest_profit = read_json(os.path.join(os.path.dirname(__file__),
                                   '10_highest_profit_test.json'))
test_10_10_lowest_p_e = read_json(os.path.join(os.path.dirname(__file__),
                                  '10_lowest_p_e_test.json'))
test_10_most_expensive_stocks = read_json(os.path.join(os.path.dirname(__file__),
                                          '10_most_expensive_stocks_test.json'))


@pytest.fixture
def mock_aioresponse():
    with aioresponses() as m:
        yield m


@pytest.mark.asyncio
def test_webscraper(mock_aioresponse, mocker):
    try:
        mocker.patch("homework10.task1.WebScraper.get_current_rate", return_value=200)
        mock_aioresponse.get('https://markets.businessinsider.com/index/components/s&p_500',
                             headers=HEADERS, payload=fake_index_html)
        mock_aioresponse.get('https://markets.businessinsider.com/index/components/s&p_500?p=1',
                             headers=HEADERS, payload=fake_index_html)
        mock_aioresponse.get('https://markets.businessinsider.com/abt',
                             headers=HEADERS, payload=fake_abt_html)
        mock_aioresponse.get('https://markets.businessinsider.com/aos',
                             headers=HEADERS, payload=fake_aos_html)
        mock_aioresponse.get('https://markets.businessinsider.com/mmm',
                             headers=HEADERS, payload=fake_mmm_html)

        data = WebScraper(current_date).parsed_data
        Data(data).create_files()

        with open(os.path.join(os.path.dirname(__file__),
                  '../../10_highest_growth.json')) as f:
            assert test_10_highest_growth == f.readlines()

        with open(os.path.join(os.path.dirname(__file__),
                  '../../10_highest_profit.json')) as f:
            assert test_10_highest_profit == f.readlines()

        with open(os.path.join(os.path.dirname(__file__),
                  '../../10_lowest_p_e_.json')) as f:
            assert test_10_10_lowest_p_e == f.readlines()

        with open(os.path.join(os.path.dirname(__file__),
                  '../../10_most_expensive_stocks_.json')) as f:
            assert test_10_most_expensive_stocks == f.readlines()
    finally:
        os.remove('10_highest_growth.json')
        os.remove('10_highest_profit.json')
        os.remove('10_lowest_p_e_.json')
        os.remove('10_most_expensive_stocks_.json')
