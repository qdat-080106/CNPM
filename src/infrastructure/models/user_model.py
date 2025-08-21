from sqlalchemy import Column, Integer, String, DateTime, Boolean
from infrastructure.databases.base import Base

class UserModel(Base):
    """
    SQLAlchemy model for the 'users' table.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=True)
    disabled = Column(Boolean, default=False)
    role = Column(String(50), nullable=False) # 'Customer', 'Dentist', 'ClinicOwner', 'Admin'
    created_at = Column(DateTime)
    updated_at = Column(DateTime)