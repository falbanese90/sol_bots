import requests
import time
import json


numer = 1000000000
x = 1

while x == 1:
    with open('symbols.json', 'r') as file:
        symbols = json.load(file)['symbols']
    for sym in symbols:
        result = requests.get(f'http://api-mainnet.magiceden.dev/v2/collections/{sym}/stats').json()
        data = {"floor": (result['floorPrice'] / numer),
                "listed_count": result['listedCount'],
                "symbol": result['symbol']}
        requests.post('http://localhost:3000/cets/add', json=data)
    time.sleep(60)