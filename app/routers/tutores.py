from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.tutor import Tutor as TutorModel
from app.schemas.tutor import Tutor as TutorSchema, TutorCreate

router = APIRouter()

@router.post("/", response_model=TutorSchema)
def criar_tutor(tutor: TutorCreate, db: Session = Depends(get_db)):
    novo_tutor = TutorModel(**tutor.dict())
    db.add(novo_tutor)
    db.commit()
    db.refresh(novo_tutor)
    return novo_tutor


