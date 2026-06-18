from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.models.animal import Animal as AnimalModel
from app.schemas.animal import Animal as AnimalSchema, AnimalCreate

router = APIRouter()

@router.get("/", response_model=list[AnimalSchema])
def listar_animais(db: Session = Depends(get_db)):
    return db.query(AnimalModel).all()

@router.get("/{animal_id}", response_model=AnimalSchema)
def obter_animal(animal_id: int, db: Session = Depends(get_db)):
    animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal

@router.post("/", response_model=AnimalSchema)
def criar_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    novo_animal = AnimalModel(**animal.dict())
    db.add(novo_animal)
    db.commit()
    db.refresh(novo_animal)
    return novo_animal

@router.put("/{animal_id}", response_model=AnimalSchema)
def atualizar_animal(animal_id: int, dados: AnimalCreate, db: Session = Depends(get_db)):
    animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    for key, value in dados.dict().items():
        setattr(animal, key, value)
    db.commit()
    db.refresh(animal)
    return animal

@router.delete("/{animal_id}")
def deletar_animal(animal_id: int, db: Session = Depends(get_db)):
    animal = db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    db.delete(animal)
    db.commit()
    return {"message": "Animal deletado com sucesso"}
