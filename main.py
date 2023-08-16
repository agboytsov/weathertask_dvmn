import os
import requests



def get_weather_from_wttr(city: str = 'san francisco') -> str:
    """Function gets information about weather in specified city/place.
    The result is in Russian, metrical, black-and-white format"""
    link = 'https://wttr.in/'
    payload = {
        'lang': 'ru',
        'm': '',
        'M': '',
        'n': '',
        'q': '',
        'T': ''
    }
    try:
        response = requests.get(f'{link}{city}', params=payload)
        response.raise_for_status()
        return response.text

    except Exception as ex:
        return f'Произошла ошибка:\n {ex}'  # The result can be printed or stored somehow else
