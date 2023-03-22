import yfinance as yf
from datetime import datetime
from src.app.send_to_kafka import publish_message
from src.config import companies_tpl


def get_historical_data():
    companies_tcrs = yf.Tickers(' '.join(companies_tpl))
    for company_name in companies_tpl:
        df = companies_tcrs.tickers[company_name].history(period="1y", interval="1d").reset_index()
        print(df.info())
        for _, row in df.iterrows():
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
