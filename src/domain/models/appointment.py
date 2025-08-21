from datetime import datetime
from typing import Optional

class Appointment:
    def __init__(self, id: Optional[int], dentist_id: int, clinic_id: int, user_id: int, date: str, time: str, result: Optional[str] = None):
        self.id = id
        self.dentist_id = dentist_id
        self.clinic_id = clinic_id
        self.user_id = user_id
        self.date = date
        self.time = time
        self.result = result