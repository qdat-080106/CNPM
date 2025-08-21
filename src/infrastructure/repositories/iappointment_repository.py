from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.appointment import Appointment

class IAppointmentRepository(ABC):
    @abstractmethod
    def add(self, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def get_by_id(self, appointment_id: int) -> Optional[Appointment]:
        pass

    @abstractmethod
    def update(self, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def delete(self, appointment_id: int) -> None:
        pass