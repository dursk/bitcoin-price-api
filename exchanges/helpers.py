from datetime import datetime

import requests


def get_datetime():
    return datetime.now().strftime('%Y-%m-%d')

def get_response(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
