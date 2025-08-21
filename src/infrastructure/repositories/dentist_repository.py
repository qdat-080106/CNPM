from domain.models.dentist import Dentist
from .identist_repository import IDentistRepository
from typing import List, Optional

class DentistRepository(IDentistRepository):
    def __init__(self):
        self._dentists = []
        self._id_counter = 1

    def add(self, dentist: Dentist) -> Dentist:
        dentist.id = self._id_counter
        self._id_counter += 1
        self._dentists.append(dentist)
        return dentist

    def get_by_id(self, dentist_id: int) -> Optional[Dentist]:
        for dentist in self._dentists:
            if dentist.id == dentist_id:
                return dentist
        return None

    def list(self) -> List[Dentist]:
        return self._dentists

    def update(self, dentist: Dentist) -> Dentist:
        for idx, d in enumerate(self._dentists):
            if d.id == dentist.id:
                self._dentists[idx] = dentist
                return dentist
        raise ValueError('Dentist not found')