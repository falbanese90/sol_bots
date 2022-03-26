import requests
import time

numer = 1000000000
x = 1

while x == 1:
    result = requests.get('http://api-mainnet.magiceden.dev/v2/collections/cets_on_creck/stats').json()
    data = {"floor": (result['floorPrice'] / numer),
            "listed_count": result['listedCount'],
            "symbol": result['symbol']}

    requests.post('http://localhost:3000/cets/add', json=data)
    time.sleep(60)