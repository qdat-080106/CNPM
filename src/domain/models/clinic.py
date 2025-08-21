from typing import Optional

class Clinic:
    def __init__(self, id: Optional[int], name: str, address: str):
        self.id = id
        self.name = name
        self.address = address