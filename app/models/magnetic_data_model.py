from base_model import SensorDataBase

class MagneticDataModel(SensorDataBase):
    flux_density_tesla: float
    axis: str
    field_direction: str