import sys
import json
import pandas as pd
import requests

print("Running: ", __file__)
print("In: ", sys.prefix)

def get_exchange_data(key, exchange='NYSE'):
    """
    returns metadata for specific exchange
    available: US, NASDAQ, OTCBB, PINK, BATS
    """
    endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/"
    endpoint += f"{exchange}?api_token={key}&fmt=json"
    print("Downloading stock data...")
    call = requests.get(endpoint).text
    exchange_data = pd.DataFrame(json.loads(call))
    print("Finished!")
    return exchange_data

def main():
    key = open('api_token.txt').read()
    print(get_exchange_data(key))

if __name__ == '__main__':
    main()

# TODO: iterate over each exchange
# TODO: output into json file named [exchange].json