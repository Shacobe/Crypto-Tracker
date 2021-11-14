# This program returns the statistics from a request for BTC, ETH and XRP cryptocurrencies
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol': 'BTC,ETH,XRP'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your-key-here',
}

# Creates a session which loads the data into json format
session = Session()
session.headers.update(headers)
try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    # Converts json to string and prints each the price for each crypto
    data_str = json.dumps(data)
    values = data_str.split(",")
    symbol_list = []
    price_list = []
    num = 0

    for item in values:

        # Records the symbol and current price of the cryptocurrencies from the data
        if "symbol" in item:
            symbol_str = item[10:]
            symbol_list.append(symbol_str)

        if "price" in item:
            price_str = item[19:]
            price_list.append(price_str)

    for item in symbol_list:
        print("Current " + item + " price is:")
        print(price_list[num] + " USD")
        print("\n")
        num = num + 1
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
