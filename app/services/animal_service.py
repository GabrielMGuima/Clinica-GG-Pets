from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.animal_repository import AnimalRepository
from app.schemas.animal import AnimalCreate, AnimalUpdate
from app.models.animal import Animal as AnimalModel

class AnimalService:
    def __init__(self, db: Session):
        self.repository = AnimalRepository(db)

    def criar_animal(self, animal: AnimalCreate) -> AnimalModel:
        return self.repository.criar(animal)

    def listar_animais(self, skip: int = 0, limit: int = 10) -> list[AnimalModel]:
        return self.repository.listar_todos(skip=skip, limit=limit)

    def buscar_animal(self, animal_id: int) -> AnimalModel:
        animal = self.repository.buscar_por_id(animal_id)
        if not animal:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Animal com ID {animal_id} não encontrado."
            )
        return animal 

    def atualizar_animal(self, animal_id: int, animal_dados: AnimalUpdate) -> AnimalModel:
        self.buscar_animal(animal_id)  # Força o 404 se não existir
        return self.repository.atualizar(animal_id, animal_dados)

    def deletar_animal(self, animal_id: int) -> None:
        animal = self.buscar_animal(animal_id)  # Força o 404 se não existir
        self.repository.deletar(animal)