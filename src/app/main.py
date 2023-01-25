import requests
from requests.exceptions import RequestException
from src.config import BASE_URL, API_KEY
from .database import quotes
from datetime import datetime


def get_info():
    companies_list = ('AAPL', 'IBM',)
    querystring = {'symbol': None, 'token': API_KEY}

    for company in companies_list:
        querystring['symbol'] = company
        try:
            response = requests.request(
                "GET",
                url=BASE_URL,
                params=querystring
            )
        except RequestException:
            print('Request Exception')
        else:
            current_price = response.json().get('c')
            current_date = str(datetime.now())
            quote = {'company': company,
                     'quote': current_price,
                     'date': current_date}

            print(quote)
            quotes.insert_one(quote)

            print(f'Added {company} info to db')

    print('Records amount:', quotes.count_documents({}))
    print('Apple records:', quotes.count_documents({'company': 'AAPL'}))

    for quote in quotes.find({'company': 'AAPL'}).sort('date'):
        print(quote, end=' ')
