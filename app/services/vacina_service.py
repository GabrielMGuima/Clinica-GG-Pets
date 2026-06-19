from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.vacina_repository import VacinaRepository
from app.schemas.vacina import VacinaCreate, VacinaUpdate
from app.models.vacina import Vacina as VacinaModel

class VacinaService:
    def __init__(self, db: Session):
        self.repository = VacinaRepository(db)

    def criar_vacina(self, vacina: VacinaCreate) -> VacinaModel:
        return self.repository.criar(vacina)

    def listar_vacinas(self, skip: int = 0, limit: int = 10) -> list[VacinaModel]:
        return self.repository.listar_todos(skip=skip, limit=limit)

    def buscar_vacina(self, vacina_id: int) -> VacinaModel:
        vacina = self.repository.buscar_por_id(vacina_id)
        if not vacina:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vacina com ID {vacina_id} não encontrada."
            )
        return vacina

    def atualizar_vacina(self, vacina_id: int, vacina_dados: VacinaUpdate) -> VacinaModel:
        self.buscar_vacina(vacina_id)
        return self.repository.atualizar(vacina_id, vacina_dados)

    def deletar_vacina(self, vacina_id: int) -> None:
        vacina = self.buscar_vacina(vacina_id)
        self.repository.deletar(vacina)