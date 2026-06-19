from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.animal import AnimalCreate, Animal, AnimalUpdate
from app.services.animal_service import AnimalService
from app.core.database import get_db

# REMOVEMOS O PREFIXO E TAGS DAQUI
router = APIRouter()

@router.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
def criar_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    service = AnimalService(db)
    return service.criar_animal(animal)

@router.get("/", response_model=List[Animal])
def listar_animais(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = AnimalService(db)
    return service.listar_animais(skip=skip, limit=limit)

@router.get("/{animal_id}", response_model=Animal)
def buscar_animal(animal_id: int, db: Session = Depends(get_db)):
    service = AnimalService(db)
    return service.buscar_animal(animal_id)

@router.put("/{animal_id}", response_model=Animal)
def atualizar_animal(animal_id: int, animal_dados: AnimalUpdate, db: Session = Depends(get_db)):
    service = AnimalService(db)
    return service.atualizar_animal(animal_id, animal_dados)

@router.delete("/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_animal(animal_id: int, db: Session = Depends(get_db)):
    service = AnimalService(db)
    service.deletar_animal(animal_id)
    return None