import requests
import json

endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

query_params = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '98a71e73-3882-4e4d-838c-925f8d01231a',
}

response = requests.get(endpoint, params=query_params, headers=headers)
data = response.json()["data"]

symbol_in = input(str("Ingrese el simbolo de la criptomoneda: "))

for info in data:
  symbol = info["symbol"]
  quote = info["quote"]
  usd = quote["USD"]
  price = usd["price"]

  if symbol_in.lower()==symbol.lower():
    print(f"[El precio de {symbol_in.upper()} es ${price}]")