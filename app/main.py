from fastapi import FastAPI
from app.routers import animais, tutores, consultas, vacinas
import logging

logging.basicConfig(level=logging.DEBUG)


app = FastAPI(
    title=" Clinica GG Pets",
    description="API para gerenciamento de clínica veterinária",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Clinica GG Pets API está funcionando!"}

app.include_router(animais.router, prefix="/animais", tags=["Animais"])
app.include_router(tutores.router, prefix="/tutores", tags=["Tutores"])
app.include_router(consultas.router, prefix="/consultas", tags=["Consultas"])
app.include_router(vacinas.router, prefix="/vacinas", tags=["Vacinas"])