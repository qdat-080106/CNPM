from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from infrastructure.databases.base import Base

class AppointmentModel(Base):
    __tablename__ = 'appointments'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    dentist_id = Column(Integer, ForeignKey('dentists.id'))
    clinic_id = Column(Integer, ForeignKey('clinics.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(String(50), nullable=False)
    time = Column(String(50), nullable=False)
    result = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)