import requests
import json


def apicoins():
    coins = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker/")
    data = json.loads(coins.text)
    coins_data = json.dumps(data, indent=2)
    if coins_data is None:
        print('Sem retorno')
    return coins_data



with open('arquivo.txt', 'w+') as f:
    f.write(apicoins())

with open('arquivo.txt','r') as f:
    resultado = f.read()
print(resultado)