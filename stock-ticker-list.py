import sys

print("Running: ", __file__)
print("In: ", sys.prefix)
print("stock tickers!")
""" from yahooquery import Ticker

ticker_list = ["GOOG", "AMZN", "SAVE"]
all_symbols = " ".join(ticker_list)
myInfo = Ticker(all_symbols)
myDict = myInfo.price

for ticker in ticker_list:
    ticker = str(ticker)
    longName = myDict[ticker]['longName']
    market_cap = myDict[ticker]['marketCap']
    price = myDict[ticker]['regularMarketPrice']
    print(ticker, longName, market_cap, price) """