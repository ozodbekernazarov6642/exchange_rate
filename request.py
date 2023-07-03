import requests

from print import order_uprinting

API_KEY = '0bcb03ab8eb32bce0176ecc5'


def get_conversion_rate_and_time(currency='USD'):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS'
    r = requests.get(url)
    res = r.json()
    conversion_rate = res['conversion_rate']
    time_lost_u = res['time_last_update_utc']
    base_code = res['base_code']

    return order_uprinting(base_code, conversion_rate, time_lost_u)


