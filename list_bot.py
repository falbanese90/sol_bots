import requests
import time
import config
import json

for symbol in config.symbol_list:
    result = result = requests.get(f'http://api-mainnet.magiceden.dev/v2/collections/{symbol}/listings?offset=0&limit=20').json()
    c = 0 
    for n in result:
        c += n['price']
    c /= len(result)
    stats = requests.get(f'http://api-mainnet.magiceden.dev/v2/collections/{symbol}/stats').json()
    floor = stats['floorPrice'] / 1000000000
    perc = round(((c / floor) * 100), 2)
    print(f'{symbol}: %{perc} -- floor: {floor}')


