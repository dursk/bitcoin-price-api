#!/usr/bin/python3

from exchanges.bitfinex import Bitfinex
price = Bitfinex.get_current_price()
print(price)
