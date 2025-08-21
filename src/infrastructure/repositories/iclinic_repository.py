from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.clinic import Clinic
from domain.models.service import Service

class IClinicRepository(ABC):
    @abstractmethod
    def list_clinics(self) -> List[Clinic]:
        pass

    @abstractmethod
    def add_clinic(self, clinic: Clinic) -> Clinic:
        pass
    
    @abstractmethod
    def list_services_by_clinic(self, clinic_id: int) -> List[Service]:
        pass

    @abstractmethod
    def add_service(self, service: Service) -> Service:
        pass