from pydantic import BaseModel

class SensorDataBase(BaseModel):
    device_id: str
    timestamp: str
    sensor_type: str
    latitude: float
    longitude: float
    status: str