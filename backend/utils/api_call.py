from requests import get

from .. import ForecastType



def api_call(
        api_key:str, 
        location:str, 
        type: ForecastType, 
        base_url:str="http://api.openweathermap.org/data/2.5/", 
        ) -> dict:
    url = f'{base_url}{type.value}'
    #?q={location}&appid={api_key}&units=metric'
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {'error': response.request.url}