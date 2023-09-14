import requests

def get_exchange_rate(api_key, from_currency, to_currency, amount):
    base_url = 'https://api.apilayer.com/exchangerates_data/convert'
    params = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
    }
    headers = {
        'apikey': api_key,
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        result = data.get('result')
        return result
    else:
        return None

