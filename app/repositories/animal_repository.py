from sqlalchemy.orm import Session
from typing import Optional
from app.models.animal import Animal as AnimalModel
from app.schemas.animal import AnimalCreate, AnimalUpdate

class AnimalRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, animal: AnimalCreate) -> AnimalModel:
        novo_animal = AnimalModel(
            nome=animal.nome,
            especie=animal.especie,
            idade=animal.idade, 
            tutor_id=animal.tutor_id
        )
        self.db.add(novo_animal)
        self.db.commit()
        self.db.refresh(novo_animal)
        return novo_animal

    def listar_todos(self, skip: int = 0, limit: int = 10) -> list[AnimalModel]:
        return self.db.query(AnimalModel).offset(skip).limit(limit).all()

    def buscar_por_id(self, animal_id: int) -> Optional[AnimalModel]:
        return self.db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()

    def atualizar(self, animal_id: int, animal_dados: AnimalUpdate) -> AnimalModel:
        db_animal = self.db.query(AnimalModel).filter(AnimalModel.id == animal_id).first()
        if db_animal:
            dados = animal_dados.model_dump(exclude_unset=True)
            for chave, valor in dados.items():
                setattr(db_animal, chave, valor)
            self.db.commit()
            self.db.refresh(db_animal)
        return db_animal

    def deletar(self, animal: AnimalModel) -> None:
        self.db.delete(animal)
        self.db.commit()