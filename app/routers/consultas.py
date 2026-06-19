from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.consulta import ConsultaCreate, Consulta
from app.services.consulta_service import ConsultaService
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=Consulta, status_code=status.HTTP_201_CREATED)
def criar_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db)):
    service = ConsultaService(db)
    return service.criar_consulta(consulta)

@router.get("/", response_model=List[Consulta])
def listar_consultas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = ConsultaService(db)
    return service.listar_consultas(skip=skip, limit=limit)

@router.get("/{consulta_id}", response_model=Consulta)
def buscar_consulta(consulta_id: int, db: Session = Depends(get_db)):
    service = ConsultaService(db)
    return service.buscar_consulta(consulta_id)

@router.delete("/{consulta_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_consulta(consulta_id: int, db: Session = Depends(get_db)):
    service = ConsultaService(db)
    service.deletar_consulta(consulta_id)
    return None