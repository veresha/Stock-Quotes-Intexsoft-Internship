import requests


def get_info(url):
    response = requests.get(url=url)
    print(response.text)
