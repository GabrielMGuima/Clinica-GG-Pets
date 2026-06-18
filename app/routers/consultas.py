from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.models.consulta import Consulta as ConsultaModel
from app.schemas.consulta import Consulta as ConsultaSchema, ConsultaCreate

router = APIRouter()

@router.get("/", response_model=list[ConsultaSchema])
def listar_consultas(db: Session = Depends(get_db)):
    return db.query(ConsultaModel).all()

@router.get("/{consulta_id}", response_model=ConsultaSchema)
def obter_consulta(consulta_id: int, db: Session = Depends(get_db)):
    consulta = db.query(ConsultaModel).filter(ConsultaModel.id == consulta_id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return consulta

@router.post("/", response_model=ConsultaSchema)
def criar_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db)):
    nova_consulta = ConsultaModel(**consulta.dict())
    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)
    return nova_consulta

@router.put("/{consulta_id}", response_model=ConsultaSchema)
def atualizar_consulta(consulta_id: int, dados: ConsultaCreate, db: Session = Depends(get_db)):
    consulta = db.query(ConsultaModel).filter(ConsultaModel.id == consulta_id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    for key, value in dados.dict().items():
        setattr(consulta, key, value)
    db.commit()
    db.refresh(consulta)
    return consulta

@router.delete("/{consulta_id}")
def deletar_consulta(consulta_id: int, db: Session = Depends(get_db)):
    consulta = db.query(ConsultaModel).filter(ConsultaModel.id == consulta_id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    db.delete(consulta)
    db.commit()
    return {"message": "Consulta deletada com sucesso"}
