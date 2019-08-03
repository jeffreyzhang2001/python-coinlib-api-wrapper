# coinlibcore.py
import requests
from .models.coin_data import CoinData
from .models.coin_list import CoinList
from .models.global_data import GlobalData


class Coinlib():
    BASE_URL = "https://coinlib.io/api/v1"
    def __init__(self, api_key):
        self.api_key = api_key

    # Multi-endpoint URL generator that combines base url, endpoint, api key, symbol, and pref currency
    def get_url(self, endpoint, symbol, pref_currency, order=""):

        url = f"{self.BASE_URL}{endpoint}?key={self.api_key}&pref={pref_currency}&symbol={symbol}&order={order}"
        api_response_json = (requests.get(url)).json()
        return api_response_json

    # Instantiate a coin instance with coinlib_instance.coin()
    def coin(self, coin_symbol, pref_currency="USD"):
        api_response_json = self.get_url("/coin", coin_symbol, pref_currency)
        coin_instance = CoinData(api_response_json)
        return coin_instance

    # Instantiate a coinlist instance with coinlib_instance.coinlist()
    def coinlist(self, pref_currency="USD", sort_type="rank_asc"):
        api_response_json = self.get_url("/global", "", pref_currency, sort_type)
        coinlist_instance = CoinList(api_response_json)
        return coinlist_instance

    # Instantiate a globalmarket instance with coinlib_instance.globalmarket()
    def globalmarket(self, pref_currency="USD"):
        api_response_json = self.get_url("/global", "", pref_currency)
        globalmarket_instance = GlobalData(api_response_json)
        return globalmarket_instance

    