from sqlalchemy.orm import Session
from typing import Optional
from app.models.consulta import Consulta as ConsultaModel
from app.schemas.consulta import ConsultaCreate

class ConsultaRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, consulta: ConsultaCreate) -> ConsultaModel:
        # Corrigido para corresponder exatamente ao seu Model de Consulta
        nova_consulta = ConsultaModel(
            data=consulta.data,          # Corrigido de data_hora para data
            descricao=consulta.descricao,# Corrigido de motivo/diagnostico para descricao
            tutor_id=consulta.tutor_id,  # Incluído tutor_id
            animal_id=consulta.animal_id
        )
        self.db.add(nova_consulta)
        self.db.commit()
        self.db.refresh(nova_consulta)
        return nova_consulta

    def listar_todos(self, skip: int = 0, limit: int = 10) -> list[ConsultaModel]:
        return self.db.query(ConsultaModel).offset(skip).limit(limit).all()

    def buscar_por_id(self, consulta_id: int) -> Optional[ConsultaModel]:
        return self.db.query(ConsultaModel).filter(ConsultaModel.id == consulta_id).first()

    def deletar(self, consulta: ConsultaModel) -> None:
        self.db.delete(consulta)
        self.db.commit()