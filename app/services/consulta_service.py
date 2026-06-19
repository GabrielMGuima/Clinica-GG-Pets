from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.consulta_repository import ConsultaRepository
from app.schemas.consulta import ConsultaCreate
from app.models.consulta import Consulta as ConsultaModel

class ConsultaService:
    def __init__(self, db: Session):
        self.repository = ConsultaRepository(db)

    def criar_consulta(self, consulta: ConsultaCreate) -> ConsultaModel:
        return self.repository.criar(consulta)

    def listar_consultas(self, skip: int = 0, limit: int = 10) -> list[ConsultaModel]:
        return self.repository.listar_todos(skip=skip, limit=limit)

    def buscar_consulta(self, consulta_id: int) -> ConsultaModel:
        consulta = self.repository.buscar_por_id(consulta_id)
        if not consulta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Consulta com ID {consulta_id} não encontrada."
            )
        return consulta

    def deletar_consulta(self, consulta_id: int) -> None:
        consulta = self.buscar_consulta(consulta_id)
        self.repository.deletar(consulta)