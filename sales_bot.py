import requests
import config
import time

buys = []
x = 1
sym = config.symbol

while x == 1:
    result = requests.get(f'http://api-mainnet.magiceden.dev/v2/collections/{sym}/activities?offset=0&limit=100').json()
    for item in result:
        if item['type'] == 'buyNow' and item not in buys:
            buys.append(item)
            print(f'Item sold for {item["price"]}')
            time.sleep(1)