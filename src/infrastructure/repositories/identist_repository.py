from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.dentist import Dentist

class IDentistRepository(ABC):
    @abstractmethod
    def list(self) -> List[Dentist]:
        pass

    @abstractmethod
    def get_by_id(self, dentist_id: int) -> Optional[Dentist]:
        pass

    @abstractmethod
    def update(self, dentist: Dentist) -> Dentist:
        pass