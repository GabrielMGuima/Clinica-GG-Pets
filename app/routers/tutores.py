from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.tutor_service import TutorService
from app.schemas.tutor import Tutor as TutorSchema, TutorCreate

router = APIRouter()

@router.post("/", response_model=TutorSchema, status_code=status.HTTP_201_CREATED)
def criar_tutor(tutor: TutorCreate, db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.criar_tutor(tutor)

@router.get("/{tutor_id}", response_model=TutorSchema)
def buscar_tutor(tutor_id: int, db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.buscar_tutor(tutor_id)

@router.get("/", response_model=list[TutorSchema])
def listar_tutores(db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.listar_tutores()

@router.get("/{tutor_id}/animais")
def listar_animais_do_tutor(tutor_id: int, db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.listar_animais_do_tutor(tutor_id)

@router.delete("/{tutor_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_apenas_tutor(tutor_id: int, db: Session = Depends(get_db)):
    service = TutorService(db)
    return service.deletar_apenas_tutor(tutor_id)