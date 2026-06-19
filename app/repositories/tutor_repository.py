from sqlalchemy.orm import Session
from typing import Optional
from app.models.tutor import Tutor as TutorModel
from app.models.animal import Animal as AnimalModel
from app.schemas.tutor import TutorCreate

class TutorRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, tutor: TutorCreate) -> TutorModel:
        novo_tutor = TutorModel(**tutor.dict())
        self.db.add(novo_tutor)
        self.db.commit()
        self.db.refresh(novo_tutor)
        return novo_tutor

    def listar_todos(self) -> list[TutorModel]:
        return self.db.query(TutorModel).all()

    def buscar_por_id(self, tutor_id: int) -> Optional[TutorModel]:  # <-- Corrigido aqui
        return self.db.query(TutorModel).filter(TutorModel.id == tutor_id).first()

    def desvincular_animais(self, tutor_id: int):
        self.db.query(AnimalModel).filter(AnimalModel.tutor_id == tutor_id).update({"tutor_id": None})

    def deletar(self, tutor: TutorModel):
        self.db.delete(tutor)
        self.db.commit()

    def buscar_animais_do_tutor(self, tutor_id: int) -> list[AnimalModel]:
        return self.db.query(AnimalModel).filter(AnimalModel.tutor_id == tutor_id).all()