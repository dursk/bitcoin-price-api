from exchange import Exchange

class Bitstamp(Exchange):
    api_url = 'https://bitstamp.net/api/ticker/'
    api_map = {
        'price': 'last',
        'bid': 'bid',
        'ask': 'ask'
    }