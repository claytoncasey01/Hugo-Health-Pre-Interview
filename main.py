import urllib.parse
import urllib.request
import json
import sys
import os

# Parse in list of coin names to sybmol json file. 
with open('coins.json') as f:
    coin_list = json.load(f)

if len(sys.argv) >= 2:
    # get the argument passed and get the symbol
    coin = sys.argv[1].strip().lower()
else: 
    print("Cryptocurrency name required but none passed")
    sys.exit()

try:
    symbol = coin_list[coin]
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={}'.format(symbol)
    headers = { 'X-CMC_PRO_API_KEY': os.environ['API_KEY'] }

    # make a request to CoinMarket
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read())

    # Extract the data we need
    coin_data = res['data'][symbol]
    USD_info = coin_data['quote']['USD']

    print('USD Price: {}'.format(USD_info['price']))
    print('USD Market Cap: {}'.format(USD_info['market_cap']))
except KeyError:
    print("Cryptocurrency not found.")
