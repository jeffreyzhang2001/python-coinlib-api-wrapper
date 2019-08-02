# coinlibcore.py
import requests
from .models.coin_data import CoinData

class Coinlib():
    BASE_URL = "https://coinlib.io/api/v1"
    def __init__(self, api_key):
        self.api_key = api_key

    # Multi-endpoint URL generator that combines base url, endpoint, api key, symbol, and pref currency
    def get_url(self, endpoint, symbol, pref_currency):
        url = f"{self.BASE_URL}{endpoint}?key={self.api_key}&pref={pref_currency}&symbol={symbol}"
        api_response_json = (requests.get(url)).json()
        return api_response_json

    # Instantiate a coin_instance with coinlib_instance.coin()
    def coin(self, coin_symbol, pref_currency="USD"):
        api_response_json = self.get_url("/coin", coin_symbol, pref_currency)
        coin_instance = CoinData(api_response_json)
        return coin_instance
