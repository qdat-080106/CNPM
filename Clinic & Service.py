# main.py — Clinic & Service (GET/POST only)
from datetime import datetime
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Query
from sqlmodel import SQLModel, Field, Session, select, create_engine

# =============== Models ===============
class Clinic(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    address: str
    city: str = Field(index=True)
    phone: Optional[str] = None
    owner_id: Optional[int] = Field(default=None, index=True)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ClinicCreate(SQLModel):
    name: str
    address: str
    city: str
    phone: Optional[str] = None
    owner_id: Optional[int] = None

class ClinicRead(SQLModel):
    id: int
    name: str
    address: str
    city: str
    phone: Optional[str]
    owner_id: Optional[int]
    is_active: bool
    created_at: datetime


class Service(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    clinic_id: int = Field(foreign_key="clinic.id", index=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    price: float = Field(ge=0)
    duration_min: int = Field(ge=5, description="Thời lượng dịch vụ (phút)")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ServiceCreate(SQLModel):
    clinic_id: int
    name: str
    description: Optional[str] = None
    price: float
    duration_min: int

class ServiceRead(SQLModel):
    id: int
    clinic_id: int
    name: str
    description: Optional[str]
    price: float
    duration_min: int
    is_active: bool
    created_at: datetime


# =============== App / DB ===============
app = FastAPI(title="Clinic & Service API (GET/POST only)")
engine = create_engine("sqlite:///./app.db", connect_args={"check_same_thread": False})

@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)


# =============== Endpoints ===============

# 1) GET /clinics
@app.get("/clinics", response_model=List[ClinicRead])
def list_clinics(
    city: Optional[str] = Query(None, description="Lọc theo thành phố"),
    ownerId: Optional[int] = Query(None, alias="ownerId", description="Lọc theo chủ phòng khám"),
    active: Optional[bool] = Query(None, description="Lọc theo trạng thái hoạt động"),
    skip: int = 0,
    limit: int = 100,
):
    with Session(engine) as s:
        stmt = select(Clinic)
        if city:
            stmt = stmt.where(Clinic.city.ilike(f"%{city}%"))
        if ownerId is not None:
            stmt = stmt.where(Clinic.owner_id == ownerId)
        if active is not None:
            stmt = stmt.where(Clinic.is_active == active)
        stmt = stmt.offset(skip).limit(min(limit, 200))
        return s.exec(stmt).all()

# 2) POST /clinics
@app.post("/clinics", response_model=ClinicRead, status_code=201)
def create_clinic(payload: ClinicCreate):
    with Session(engine) as s:
        clinic = Clinic(**payload.dict())
        s.add(clinic)
        s.commit()
        s.refresh(clinic)
        return clinic

# 3) GET /services?clinicId=...
@app.get("/services", response_model=List[ServiceRead])
def list_services(
    clinicId: Optional[int] = Query(None, alias="clinicId", description="Lọc theo clinic"),
    q: Optional[str] = Query(None, description="Tìm theo tên dịch vụ"),
    active: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100,
):
    with Session(engine) as s:
        stmt = select(Service)
        if clinicId is not None:
            stmt = stmt.where(Service.clinic_id == clinicId)
        if q:
            stmt = stmt.where(Service.name.ilike(f"%{q}%"))
        if active is not None:
            stmt = stmt.where(Service.is_active == active)
        stmt = stmt.offset(skip).limit(min(limit, 200))
        return s.exec(stmt).all()

# 4) POST /services
@app.post("/services", response_model=ServiceRead, status_code=201)
def create_service(payload: ServiceCreate):
    with Session(engine) as s:
        if not s.get(Clinic, payload.clinic_id):
            raise HTTPException(404, "Clinic not found")
        service = Service(**payload.dict())
        s.add(service)
        s.commit()
        s.refresh(service)
        return service

@app.get("/")
def root():
    return {"ok": True, "endpoints": ["/clinics (GET, POST)", "/services (GET, POST)"], "docs": "/docs"}

