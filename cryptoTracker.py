# This program returns the url information from a request for BTC, ETH and XRP cryptocurrency statistics
import urllib.request
url = "https://api.nomics.com/v1/currencies/ticker?key=your-key-here&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&per-page=100&page=1"
print(urllib.request.urlopen(url).read())
