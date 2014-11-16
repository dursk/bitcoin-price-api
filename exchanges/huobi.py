from exchange import Exchange

class Huobi(Exchange):
    api_url = 'https://market.huobi.com/staticmarket/ticker_btc_json.js'
    api_map = {
        'price': ['ticker', 'last'],
        'bid': ['ticker', 'buy'],
        'ask': ['ticker', 'sell']
    }