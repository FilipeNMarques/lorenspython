import requests
import json


def apicoins():
    coins = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker/")
    data = coins.json()
    coins_data = json.dumps(data, indent=2)
    print(coins_data)

print(apicoins())