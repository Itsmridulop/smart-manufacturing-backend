from base_model import SensorDataBase

class VibrationDataModel(SensorDataBase):
    acceleration_x_g: float
    acceleration_y_g: float
    acceleration_z_g: float
    rms_velocity_mm_s: float
    peak_frequency_hz: float