from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class ClinicModel(Base):
    __tablename__ = 'clinics'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    services = relationship("ServiceModel", back_populates="clinic")

class ServiceModel(Base):
    __tablename__ = 'services'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    clinic_id = Column(Integer, ForeignKey('clinics.id'))
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    clinic = relationship("ClinicModel", back_populates="services")