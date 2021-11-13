# This program returns the url information from a request for cryptocurrency statistics
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# Gets the statistics of the first 5 cryptocurrencies in the latest coinmarketcap listing
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
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

    # Converts json to string and prints each individual statistic
    data_str = json.dumps(data)
    values = data_str.split(",")
    for item in values:
        print(item)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
