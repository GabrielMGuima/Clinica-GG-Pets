from pydantic import BaseModel
from typing import Optional
from datetime import date

class ConsultaBase(BaseModel):
    data: date
    descricao: str
    tutor_id: int
    animal_id: int

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(BaseModel):
    data: Optional[date] = None
    descricao: Optional[str] = None
    tutor_id: Optional[int] = None
    animal_id: Optional[int] = None

class Consulta(BaseModel):
    id: int
    data: date
    descricao: str
    tutor_id: int
    animal_id: int

    class Config:
        from_attributes = True
