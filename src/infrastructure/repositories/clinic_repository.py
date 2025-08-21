from domain.models.clinic import Clinic
from domain.models.service import Service
from .iclinic_repository import IClinicRepository
from typing import List, Optional

class ClinicRepository(IClinicRepository):
    def __init__(self):
        self._clinics = []
        self._services = []
        self._clinic_id_counter = 1
        self._service_id_counter = 1

    def list_clinics(self) -> List[Clinic]:
        return self._clinics

    def add_clinic(self, clinic: Clinic) -> Clinic:
        clinic.id = self._clinic_id_counter
        self._clinic_id_counter += 1
        self._clinics.append(clinic)
        return clinic

    def list_services_by_clinic(self, clinic_id: int) -> List[Service]:
        return [s for s in self._services if s.clinic_id == clinic_id]

    def add_service(self, service: Service) -> Service:
        service.id = self._service_id_counter
        self._service_id_counter += 1
        self._services.append(service)
        return service