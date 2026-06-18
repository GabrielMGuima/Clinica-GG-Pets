from pydantic import BaseModel
from typing import Optional
from datetime import date

class VacinaBase(BaseModel):
    nome: str
    data_aplicacao: date
    animal_id: int

class VacinaCreate(VacinaBase):
    pass

class VacinaUpdate(BaseModel):
    nome: Optional[str] = None
    data_aplicacao: Optional[date] = None
    animal_id: Optional[int] = None

class Vacina(BaseModel):
    id: int
    nome: str
    data_aplicacao: date
    animal_id: int

    class Config:
        from_attributes = True
