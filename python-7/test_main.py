import pytest

import main
from exceptions import TemperatureNotFound


@pytest.fixture
def mock_get_request_data_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return {"currently": {"temperature": 62}}

    monkeypatch.setattr(main, "__get_request_data", mock_get)


@pytest.fixture
def mock_get_request_data_null_temperature(monkeypatch):
    def mock_get(*args, **kwargs):
        return {"currently": {"temperature": None}}

    monkeypatch.setattr(main, "__get_request_data", mock_get)


def test_get_temperature_by_lat_lng(mock_get_request_data_success):
    lat = -12.235004
    lng = -59.92528

    get_temperature_expected_return = 16

    assert main.get_temperature(lat=lat, lng=lng) == get_temperature_expected_return


def test_raise_null_temperature(mock_get_request_data_null_temperature):
    lat = -12.235004
    lng = -59.92528

    with pytest.raises(TemperatureNotFound):
        assert main.get_temperature(lat=lat, lng=lng)


@pytest.mark.parametrize(
    "temperature, expected", [(32, 0), (85, 29), (117, 47), (65, 18)]
)
def test_celsius_convertion_valid(temperature, expected):
    assert main.__convert_to_celsius(temperature=temperature) == expected


@pytest.mark.parametrize("temperature", ["a", "b", True, False, [], {}, ()])
def test_celsius_convertion_invalid(temperature):
    """
    somente int e float são aceitáveis como parametro
    """
    with pytest.raises(ValueError):
        assert main.__convert_to_celsius(temperature=temperature)
