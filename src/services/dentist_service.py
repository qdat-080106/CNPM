from domain.models.dentist import Dentist
from infrastructure.repositories.identist_repository import IDentistRepository
from typing import List, Optional

class DentistService:
    def __init__(self, repository: IDentistRepository):
        self.repository = repository

    def list_all_dentists(self) -> List[Dentist]:
        return self.repository.list()

    def update_availability(self, dentist_id: int, availability_data: dict) -> Optional[Dentist]:
        dentist = self.repository.get_by_id(dentist_id)
        if dentist:
            # TODO: Cập nhật lịch làm việc của nha sĩ
            # dentist.availability = availability_data
            return self.repository.update(dentist)
        return None