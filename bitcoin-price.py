#!/usr/bin/python3

from exchanges.bitfinex import Bitfinex
from exchanges.poloniex import Poloniex
from exchanges.kraken import Kraken
from exchanges.bitmex import Bitmex
from exchanges.bitvc import BitVc
from exchanges.futures796 import Futures796

price = Bitfinex().get_current_price()
print(price)

price = Poloniex().get_current_price()
print(price)

price = Kraken().get_current_price()
print(price)

data = Bitmex().get_data()
print(data)

data = BitVc().get_data()
print(data)

