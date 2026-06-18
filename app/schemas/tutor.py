from pydantic import BaseModel
from typing import Optional

class TutorBase(BaseModel):
    nome: str
    email: str
    telefone: str

class TutorCreate(TutorBase):
    pass

class TutorUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

class Tutor(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

    class Config:
        from_attributes = True
