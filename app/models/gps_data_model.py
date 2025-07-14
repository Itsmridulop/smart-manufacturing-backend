from base_model import SensorDataBase

class GPSDataModel(SensorDataBase):
    satellites_visible: int
    hdop: float
    altitude_meters: float
    speed_kmph: float
    heading_degrees: float