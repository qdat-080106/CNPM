from domain.models.clinic import Clinic
from domain.models.service import Service
from infrastructure.repositories.iclinic_repository import IClinicRepository
from typing import List, Optional

class ClinicService:
    def __init__(self, repository: IClinicRepository):
        self.repository = repository

    def list_all_clinics(self) -> List[Clinic]:
        return self.repository.list_clinics()

    def create_clinic(self, clinic_data: dict) -> Clinic:
        clinic = Clinic(id=None, **clinic_data)
        return self.repository.add_clinic(clinic)

    def get_services_by_clinic(self, clinic_id: int) -> List[Service]:
        return self.repository.list_services_by_clinic(clinic_id)

    def create_service(self, service_data: dict) -> Service:
        service = Service(id=None, **service_data)
        return self.repository.add_service(service)