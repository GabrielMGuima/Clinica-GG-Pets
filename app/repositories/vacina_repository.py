from sqlalchemy.orm import Session
from typing import Optional
from app.models.vacina import Vacina as VacinaModel
from app.schemas.vacina import VacinaCreate, VacinaUpdate

class VacinaRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, vacina: VacinaCreate) -> VacinaModel:
        nova_vacina = VacinaModel(
            nome=vacina.nome,
            data_aplicacao=vacina.data_aplicacao,
            lote=vacina.lote,
            animal_id=vacina.animal_id
        )
        self.db.add(nova_vacina)
        self.db.commit()
        self.db.refresh(nova_vacina)
        return nova_vacina

    def listar_todos(self, skip: int = 0, limit: int = 10) -> list[VacinaModel]:
        return self.db.query(VacinaModel).offset(skip).limit(limit).all()

    def buscar_por_id(self, vacina_id: int) -> Optional[VacinaModel]:
        return self.db.query(VacinaModel).filter(VacinaModel.id == vacina_id).first()

    def atualizar(self, vacina_id: int, vacina_dados: VacinaUpdate) -> Optional[VacinaModel]:
        db_vacina = self.buscar_por_id(vacina_id)
        if db_vacina:
            dados = vacina_dados.model_dump(exclude_unset=True)
            for chave, valor in dados.items():
                setattr(db_vacina, chave, valor)
            self.db.commit()
            self.db.refresh(db_vacina)
        return db_vacina

    def deletar(self, vacina: VacinaModel) -> None:
        self.db.delete(vacina)
        self.db.commit()