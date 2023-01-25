import requests
from src.config import BASE_URL, API_KEY
from database import rates_db
from datetime import datetime


def get_info():
    companies_list = ('AAPL', 'IBM',)
    querystring = {'symbol': None, 'token': API_KEY}
    quotes = rates_db.quotes

    for company in companies_list:
        querystring['symbol'] = company
        response = requests.request(
            "GET",
            url=BASE_URL,
            params=querystring
        )
        current_price = response.json().get('c')
        print(current_price)

        quote = {'company': company,
                 'quote': current_price,
                 'date': datetime.utcnow()}

        print(quote)

        quotes.insert_one(quote)
