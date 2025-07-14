from base_model import SensorDataBase

class HumidityDataModel(SensorDataBase):
    humidity_percent: float
    temperature_celsius: float