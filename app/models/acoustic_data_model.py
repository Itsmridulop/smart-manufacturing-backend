from base_model import SensorDataBase
from typing import List

class AcousticDataModel(SensorDataBase):
   sound_level_db: float
   peak_frequency_hz: List[float]
   peak_frequency_hz: float