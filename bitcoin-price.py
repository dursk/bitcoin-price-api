#!/usr/bin/python3

from exchanges.bitfinex import Bitfinex
from exchanges.poloniex import Poloniex
from exchanges.kraken import Kraken

price = Bitfinex().get_current_price()
print(price)

price = Poloniex().get_current_price()
print(price)

price = Kraken().get_current_price()
print(price)
