from pydantic import BaseModel, ConfigDict
from typing import Optional

class AnimalBase(BaseModel):
    nome: str
    especie: str
    idade: int
    tutor_id: Optional[int] = None

class AnimalCreate(AnimalBase):
    pass

class AnimalUpdate(BaseModel):
    nome: Optional[str] = None
    especie: Optional[str] = None
    idade: Optional[int] = None
    tutor_id: Optional[int] = None

class Animal(BaseModel):
    id: int
    nome: str
    especie: str
    idade: int
    tutor_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)