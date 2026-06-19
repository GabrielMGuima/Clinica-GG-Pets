from fastapi import FastAPI, HTTPException
from app.core.database import engine, Base
from app.routers import animais, tutores, consultas, vacinas
from app.core.exceptions import handler_erro_global

# IMPORTANTE: Importar TODOS os modelos para registrar na Base
from app.models.tutor import Tutor
from app.models.animal import Animal
from app.models.vacina import Vacina
from app.models.consulta import Consulta

app = FastAPI(
    title="Clinica GG Pets",
    description="API para gerenciamento de clínica veterinária",
    version="1.0.0"
)

# Inicializa o banco de dados criando as tabelas se não existirem
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.add_exception_handler(HTTPException, handler_erro_global)

# Rotas
app.include_router(animais.router, prefix="/animais", tags=["Animais"])
app.include_router(tutores.router, prefix="/tutores", tags=["Tutores"])
app.include_router(consultas.router, prefix="/consultas", tags=["Consultas"])
app.include_router(vacinas.router, prefix="/vacinas", tags=["Vacinas"])

@app.get("/")
def root():
    return {"message": "Clinica GG Pets API está funcionando!"}