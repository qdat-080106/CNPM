from domain.models.appointment import Appointment
from infrastructure.repositories.iappointment_repository import IAppointmentRepository
from typing import Optional

class AppointmentService:
    def __init__(self, repository: IAppointmentRepository):
        self.repository = repository

    def create_appointment(self, appointment_data: dict) -> Appointment:
        appointment = Appointment(id=None, **appointment_data)
        return self.repository.add(appointment)

    def update_appointment(self, appointment_id: int, appointment_data: dict) -> Optional[Appointment]:
        appointment = self.repository.get_by_id(appointment_id)
        if appointment:
            # TODO: Cập nhật thông tin cuộc hẹn
            # appointment.update_from_dict(appointment_data)
            return self.repository.update(appointment)
        return None

    def update_result(self, appointment_id: int, result_data: dict) -> Optional[Appointment]:
        appointment = self.repository.get_by_id(appointment_id)
        if appointment:
            # TODO: Cập nhật kết quả khám
            # appointment.result = result_data['result']
            return self.repository.update(appointment)
        return None