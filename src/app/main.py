import requests
from requests.exceptions import RequestException
from src.config import BASE_URL, API_KEY
from datetime import datetime
from src.app.kafka_connection import publish_message


def get_info():
    companies_list = ('AAPL', 'AMZN', 'TSLA', 'MSFT', 'GOOG',)
    querystring = {'symbol': None, 'token': API_KEY}

    for company in companies_list:
        querystring['symbol'] = company
        try:
            response = requests.request(
                "GET",
                url=BASE_URL,
                params=querystring
            )
        except RequestException as ex:
            print('Request Exception:', str(ex))
        else:
            current_price = response.json().get('c')
            current_date = str(datetime.now())[:19]
            quote = {'company': company,
                     'quote': current_price,
                     'date': current_date}

            publish_message(quote)
