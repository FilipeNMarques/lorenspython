import requests
import json
import datetime

# EXEMPLO
"""
r = requests.get('https://api.github.com/events')
r.json()
"""


def apicoins(code):
    coins = requests.get(f"https://www.mercadobitcoin.net/api/{code}/ticker/")
    # data = json.loads(coins)
    # coins_data = json.dumps(data, indent=2)
    coins_data = coins.json()
    if coins_data is None:
        print('Sem retorno')
    return coins_data


retorno_api = apicoins('btc')

criptosdata = {'data': retorno_api['ticker']['date']}
for time in criptosdata.values():
    time_formatted = datetime.datetime.fromtimestamp(time).strftime('%d/%m/%Y')

datadict = time_formatted

criptos = {'data': (datadict), 'último preço': retorno_api['ticker']['last'],'alta': retorno_api['ticker']['high'],'baixa': retorno_api['ticker']['low'], 'volume': retorno_api['ticker']['vol']}
carteira = [criptos]
print(carteira)


def addnacarteira():
    with open('carteira.txt', 'a') as arquivo:
         for item in carteira:
             arquivo.write(str(carteira) +'\n')
    if carteira is None:
        print('sem moedas na sua carteira')
addnacarteira()
