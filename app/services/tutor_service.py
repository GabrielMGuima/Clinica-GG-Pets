from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from app.repositories.tutor_repository import TutorRepository
from app.schemas.tutor import TutorCreate
from app.models.tutor import Tutor as TutorModel
from app.models.animal import Animal as AnimalModel

class TutorService:
    def __init__(self, db: Session):
        self.repository = TutorRepository(db)

    def criar_tutor(self, tutor: TutorCreate) -> TutorModel:
        try:
            return self.repository.criar(tutor)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email já cadastrado."
            )

    def listar_tutores(self) -> list[TutorModel]:
        return self.repository.listar_todos()

    def listar_animais_do_tutor(self, tutor_id: int) -> list[AnimalModel]:
        tutor = self.repository.buscar_por_id(tutor_id)
        if not tutor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Tutor com ID {tutor_id} não encontrado."
            )
        return self.repository.buscar_animais_do_tutor(tutor_id)

    def deletar_apenas_tutor(self, tutor_id: int) -> None:
        tutor = self.repository.buscar_por_id(tutor_id)
        if not tutor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Tutor com ID {tutor_id} não encontrado."
            )
        
        self.repository.desvincular_animais(tutor_id)
        self.repository.deletar(tutor)
        return None
    
    def buscar_tutor(self, tutor_id: int):
       
        tutor = self.repository.buscar_por_id(tutor_id) 
        
        if not tutor:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Tutor não encontrado")
            
        return tutor