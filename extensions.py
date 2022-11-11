import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        quote_ticker, base_ticker = keys[quote], keys[base]
        if quote == base:
            raise ConvertionException('Неудалось конвертировать одинаковые валюты')

        try:
            quote_ticker == keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote_ticker}')

        try:
            base_ticker == keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base_ticker}')

        try:
            amount = round(float(amount))
        except ValueError:
            raise ConvertionException(f'Введите число вместо "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        text_base = json.loads(r.content)[keys[base]]

        return text_base