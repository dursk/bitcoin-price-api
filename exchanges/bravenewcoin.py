from exchanges.base import Exchange

class BraveNewCoin(Exchange):
    TICKER_URL = 'http://api.bravenewcoin.com/ticker/bnc_ticker_btc.json'

    def _current_price_extractor(self, data):
        return data['ticker']['bnc_price_index_usd']

    def get_current_bid(self):
        return None

    def get_current_ask(self):
        return None
