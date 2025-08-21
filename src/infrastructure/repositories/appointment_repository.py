from domain.models.appointment import Appointment
from .iappointment_repository import IAppointmentRepository
from typing import List, Optional

class AppointmentRepository(IAppointmentRepository):
    def __init__(self):
        self._appointments = []
        self._id_counter = 1

    def add(self, appointment: Appointment) -> Appointment:
        appointment.id = self._id_counter
        self._id_counter += 1
        self._appointments.append(appointment)
        return appointment

    def get_by_id(self, appointment_id: int) -> Optional[Appointment]:
        for appointment in self._appointments:
            if appointment.id == appointment_id:
                return appointment
        return None

    def update(self, appointment: Appointment) -> Appointment:
        for idx, a in enumerate(self._appointments):
            if a.id == appointment.id:
                self._appointments[idx] = appointment
                return appointment
        raise ValueError('Appointment not found')

    def delete(self, appointment_id: int) -> None:
        self._appointments = [a for a in self._appointments if a.id != appointment_id]