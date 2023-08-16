import requests


def get_weather_from_wttr(city: str='san francisco') -> str:
    """Function gets information about weather in specified city/place.
    The result is in Russian, metrical, black-and-white format"""
    link = 'https://wttr.in/'
    payload = {
      'lang' : 'ru', 
      'm' : '', 
      'M' : '',  
      'n' :'', 
      'q' : '', 
      'T' : ''
    }

    response = requests.get(f'{link}{city}', params = payload)
    response.raise_for_status()
    return response.text
  
    
if __name__ == "__main__":
    for place in ['london','svo','череповец']:
        try:
            print(get_weather_from_wttr(place))
        except (requests.ConnectionError, requests.HTTPError) as ex:
            print(f'Произошла ошибка:\n {ex}')
  
