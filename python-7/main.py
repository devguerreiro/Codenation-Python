import requests

from exceptions import TemperatureNotFound


def get_temperature(lat: float, lng: float) -> int:
    """
    retorna a temperatura em graus celsius com base na latitude e longitude
    """
    data = __get_request_data(lat=lat, lng=lng)
    temperature = data.get("currently").get("temperature")

    if not temperature:
        raise TemperatureNotFound()

    return __convert_to_celsius(temperature=temperature)


def __convert_to_celsius(temperature: float) -> int:
    type_parameter = type(temperature)

    if type_parameter is not int and type_parameter is not float:
        raise ValueError

    return int((temperature - 32) * 5.0 / 9.0)


def __get_request_data(*, lat: float, lng: float) -> dict:
    key = "e1ee55658d4a2b28c4841e373c3b3d87"
    url = f"https://api.darksky.net/forecast/{key}/{lat},{lng}"

    return requests.get(url).json()
