from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class VacinaBase(BaseModel):
    nome: str
    data_aplicacao: date
    lote: Optional[str] = None
    animal_id: int

class VacinaCreate(VacinaBase):
    pass

class VacinaUpdate(BaseModel):
    nome: Optional[str] = None
    data_aplicacao: Optional[date] = None
    lote: Optional[str] = None
    animal_id: Optional[int] = None

class Vacina(VacinaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)