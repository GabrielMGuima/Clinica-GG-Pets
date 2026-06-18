from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.models.vacina import Vacina as VacinaModel
from app.schemas.vacina import Vacina as VacinaSchema, VacinaCreate

router = APIRouter()

@router.get("/", response_model=list[VacinaSchema])
def listar_vacinas(db: Session = Depends(get_db)):
    return db.query(VacinaModel).all()

@router.get("/{vacina_id}", response_model=VacinaSchema)
def obter_vacina(vacina_id: int, db: Session = Depends(get_db)):
    vacina = db.query(VacinaModel).filter(VacinaModel.id == vacina_id).first()
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return vacina

@router.post("/", response_model=VacinaSchema)
def criar_vacina(vacina: VacinaCreate, db: Session = Depends(get_db)):
    nova_vacina = VacinaModel(**vacina.dict())
    db.add(nova_vacina)
    db.commit()
    db.refresh(nova_vacina)
    return nova_vacina

@router.put("/{vacina_id}", response_model=VacinaSchema)
def atualizar_vacina(vacina_id: int, dados: VacinaCreate, db: Session = Depends(get_db)):
    vacina = db.query(VacinaModel).filter(VacinaModel.id == vacina_id).first()
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    for key, value in dados.dict().items():
        setattr(vacina, key, value)
    db.commit()
    db.refresh(vacina)
    return vacina

@router.delete("/{vacina_id}")
def deletar_vacina(vacina_id: int, db: Session = Depends(get_db)):
    vacina = db.query(VacinaModel).filter(VacinaModel.id == vacina_id).first()
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    db.delete(vacina)
    db.commit()
    return {"message": "Vacina deletada com sucesso"}
