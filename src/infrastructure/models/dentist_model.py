from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class DentistModel(Base):
    __tablename__ = 'dentists'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    specialty = Column(String(255))