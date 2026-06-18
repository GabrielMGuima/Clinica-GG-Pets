from pydantic import BaseModel
from typing import Optional

class AnimalBase(BaseModel):
    nome: str
    especie: str
    tutor_id: int

class AnimalCreate(AnimalBase):
    pass

class AnimalUpdate(BaseModel):
    nome: Optional[str] = None
    especie: Optional[str] = None
    tutor_id: Optional[int] = None

class Animal(BaseModel):
    id: int
    nome: str
    especie: str
    tutor_id: int

    class Config:
        from_attributes = True
