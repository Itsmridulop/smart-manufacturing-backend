from base_model import SensorDataBase

class TemperatureDataModel(SensorDataBase):
    temperature_celsius: float
    temperature_fahrenheit: float