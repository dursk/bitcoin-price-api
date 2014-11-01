Bitcoin Price API
----------------------------------------------------------------------

If you are trying to do interesting things with bitcoin price data,
you shouldn't have to be concerned with the low-level details of how
to obtain that data, or the particular JSON structures that it comes in.
This module will provide a unified way of getting price data from various
exchanges which have publicly available API's, as well as a unified
representation of that data rather than exchange specific ones.

### Bitstamp, Bitfinex, OKCoin

All expose the interface below:

	get_current_price()
	get_current_bid()
	get_current_ask()

which will return a Decimal object.

### Coindesk

Coindesk offers a much richer price interface:

	get_current_price(currency='USD')
	get_past_price(date)
	get_historical_data_as_dict(start='2014-09-01', end=None)
	get_historical_data_as_list(start='2014-09-01', end=None

`get_current_price` and `get_past_price` both return `Decimal` objects. 
`get_current_price` takes in an optional parameter specifying the currency.
The dates for all functions must be in the form 'YYYY-MM-DD'.
`get_historical_data_as_dict` will return a dictionary of the follwing format:
	{'2014-10-20': 400.00, '2014-10-21': 301.99}
`get_historical_data_as_list` will return a list of dictionaries:
	[ {'date': 'YYYY-MM-DD', 'price': 300.00}, {'date': 'YYYY-MM-DD', 'price': 301.00 }]

