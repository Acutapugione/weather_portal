# api_call(location, ForecastType.weather)
from enum import Enum


class ForecastType(str, Enum):
    weather = "weather"
    forecast = "forecast"