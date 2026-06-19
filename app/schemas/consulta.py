from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class ConsultaBase(BaseModel):
    data: date
    descricao: str  # Ajustado para 'descricao' (igual ao seu Model)
    tutor_id: int   # Obrigatório conforme seu model
    animal_id: int

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(BaseModel):
    data: Optional[date] = None
    descricao: Optional[str] = None
    tutor_id: Optional[int] = None
    animal_id: Optional[int] = None

class Consulta(ConsultaBase):
    id: int
    # Se você for usar status, adicione aqui:
    # status: str = "AGENDADA" 
    
    model_config = ConfigDict(from_attributes=True)