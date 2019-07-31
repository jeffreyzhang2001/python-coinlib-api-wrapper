from coinlibwrapper.coinlibcore import Coinlib
from api_key import coinlib_api_key

coinlib = Coinlib(coinlib_api_key) # Initializes a Coinlib instance in order to interact with rest of wrapper
# coin_instance = coinlib.coin('symbol')
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
