from typing import Optional

class Service:
    def __init__(self, id: Optional[int], clinic_id: int, name: str, description: Optional[str] = None):
        self.id = id
        self.clinic_id = clinic_id
        self.name = name
        self.description = description