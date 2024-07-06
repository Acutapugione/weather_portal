from flask import request, jsonify

from .. import app, api_key
from backend import ForecastType, api_call


@app.get("api/v1/weather/")
def weather():
    location = request.args.get('location')
    if location and api_key:
        result = api_call(location=location, type=ForecastType.weather, api_key=api_key)
        return jsonify(result)
    return jsonify(error='Location not provided'), 400



@app.get("api/v1/forecast")
def forecast():
    location = request.args.get('location')
    if location and api_key:
        result = api_call(location=location, type=ForecastType.forecast, api_key=api_key)

        # get weather info for nearest few days
        if not result:
            return jsonify(error='Request error'), 400
        
        # forecast = []
        # for entry in result.get('list'):
        #     extracted_data = extract_weather_data(entry)
        #     forecast.append(extracted_data)

        return jsonify(result.get('list'))
    return jsonify(error='Location not provided'), 400