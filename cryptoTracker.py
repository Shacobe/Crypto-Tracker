# This program returns the url information from a request for BTC, ETH and XRP cryptocurrency statistics
import urllib.request
url = "https://api.nomics.com/v1/currencies/ticker?key=your-key-here&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&per-page=100&page=1"
file = urllib.request.urlopen(url)
url_str = (str(file.read(), 'utf-8'))

values = url_str.split(",")
id_list = []
price_list = []
num = 0;

# Prints each separate item in the url
for item in values:
    print(item)

    # Gets the id and current price of the cryptocurrencies in the URL
    if "id" in item:
        id_str = item[7:]
        id_list.append(id_str)
    if "price" in item and "date" not in item and "time" not in item and "change" not in item:
        price_str = item[8:]
        price_list.append(price_str)

for item in id_list:
    print("Current " + item + " price is:")
    print(price_list[num] + " USD")
    print("\n")
    num = num+1
