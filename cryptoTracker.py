# This program returns the url information from a request for BTC, ETH and XRP cryptocurrency statistics
import urllib.request
url = "https://api.nomics.com/v1/currencies/ticker?key=your-key-here&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&per-page=100&page=1"
file = urllib.request.urlopen(url)
url_str = (str(file.read(), 'utf-8'))

values = url_str.split(",")
crypto_str1 = ""
crypto_price_str1 = ""
first_done_id = False
first_done_price = False

# Prints each separate item in the url
for item in values:
    print(item)

    # Gets the id and current price of the first cryptocurrency in the URL
    if "id" in item and first_done_id is False:
        crypto_str1 = item[7:]
        first_done_id = not first_done_id
    if "price" in item and "date" not in item and "time" not in item and first_done_price is False:
        crypto_price_str1 = item[8:]
        first_done_price = not first_done_price

print("Current " + crypto_str1 + " price is:")
print(crypto_price_str1)
