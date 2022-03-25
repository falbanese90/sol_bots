import requests
import config
import time

sym = config.symbol
x = 1
total_listed = 0

while x == 1:
    result = requests.get(f'http://api-mainnet.magiceden.dev/v2/collections/{sym}/stats').json()
    if result['listedCount'] != total_listed:
        change = total_listed - result['listedCount']
        total_listed = result['listedCount']
        if change > 0:
            print(f'Total listed count is {total_listed}, decreased by {change}')
        elif change < 0:
            print(f'Total listed count is {total_listed}, increased by {abs(change)}')
            time.sleep(1)
