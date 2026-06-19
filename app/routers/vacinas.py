from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.vacina import VacinaCreate, Vacina, VacinaUpdate
from app.services.vacina_service import VacinaService
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=Vacina, status_code=status.HTTP_201_CREATED)
def criar_vacina(vacina: VacinaCreate, db: Session = Depends(get_db)):
    service = VacinaService(db)
    return service.criar_vacina(vacina)

@router.get("/", response_model=List[Vacina])
def listar_vacinas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = VacinaService(db)
    return service.listar_vacinas(skip=skip, limit=limit)

@router.get("/{vacina_id}", response_model=Vacina)
def buscar_vacina(vacina_id: int, db: Session = Depends(get_db)):
    service = VacinaService(db)
    return service.buscar_vacina(vacina_id)

@router.put("/{vacina_id}", response_model=Vacina)
def atualizar_vacina(vacina_id: int, vacina_dados: VacinaUpdate, db: Session = Depends(get_db)):
    service = VacinaService(db)
    return service.atualizar_vacina(vacina_id, vacina_dados)

@router.delete("/{vacina_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_vacina(vacina_id: int, db: Session = Depends(get_db)):
    service = VacinaService(db)
    service.deletar_vacina(vacina_id)
    return None