# coinlibcore.py
import requests
from .models import coin_data

class Coinlib():
    BASE_URL = "https://coinlib.io/api/v1"
    def __init__(self, api_key): # A Coinlib API key. More info at: https://coinlib.io/apidocs.
        self.api_key = api_key

    def get_url(self, endpoint, symbol, pref_currency="USD"):
        url = f"{self.BASE_URL}{endpoint}?key={self.api_key}&pref={pref_currency}&symbol={symbol}"
        return(url)
        #api_response_json = (requests.get(url)).json()
        #return(api_response_json["price"]+f" {symbol}")

    # When called on Coinlib instance, creates Coin instance
    def coin(self, coin_symbol):
        # Creates an object using imported coin_data class
        # This object must contain the following functionality:
            # coin_instance.name
            # coin_instance.symbol
            # coin_instance.price
            # coin_instance.rank
            # coin_instance.market_cap
            # coin_instance.total_volume_24h
            # coin_instance.high_24h
            # coin_instance.low_24h
            # coin_instance.delta_1h
            # coin_instance.delta_24h
            # coin_instance.delta_7d
            # coin_instance.delta_30d
        pass
