from datetime import datetime
from typing import Optional

class Dentist:
    def __init__(self, id: Optional[int], name: str, specialty: str, availability: Optional[list] = None):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.availability = availability if availability else []