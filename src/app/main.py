import random
import requests
import yfinance as yf
from requests.exceptions import RequestException
from src.config import BASE_URL, API_KEY
from datetime import datetime, timedelta
from src.app.kafka_connection import publish_message

companies_tpl = ('AAPL', 'AMZN', 'TSLA', 'MSFT', 'GOOG',)


def get_historical_data():
    companies_tcrs = yf.Tickers('AAPL AMZN TSLA MSFT GOOG')
    for company_name in companies_tpl:
        df = companies_tcrs.tickers[company_name].history(period="1y", interval="1d").reset_index()
        for index, row in df.iterrows():
            current_price = float(row['Close'])
            current_date = str(row['Date'])[:19]
            quote = {'company': company_name,
                     'quote': current_price,
                     'date': current_date}
            print(quote)

            publish_message(quote)


def get_info_from_yahoo():
    for company_name in companies_tpl:
        company_tcr = yf.Ticker(company_name)
        current_price = dict(company_tcr.fast_info.items()).get("lastPrice", 'no_data')
        current_date = str(datetime.now())[:19]
        quote = {'company': company_name,
                 'quote': current_price,
                 'date': current_date}

        publish_message(quote)


def auto_filling_info():
    for company in companies_tpl:
        current_price = round(random.uniform(100.0, 150.0), 2)
        start_date = datetime.now()
        date = str(start_date + timedelta(random.randint(0, timedelta(days=30).days)))[:19]
        quote = {'company': company,
                 'quote': current_price,
                 'date': date}
        publish_message(quote)


def get_info_from_api():
    querystring = {'symbol': None, 'token': API_KEY}
    for company in companies_tpl:
        querystring['symbol'] = company
        try:
            response = requests.request(
                "GET",
                url=BASE_URL,
                params=querystring)
        except RequestException as ex:
            print('Request Exception:', str(ex))
        else:
            current_price = response.json().get('c')
            current_date = str(datetime.now())[:19]
            quote = {'company': company,
                     'quote': current_price,
                     'date': current_date}

            publish_message(quote)
