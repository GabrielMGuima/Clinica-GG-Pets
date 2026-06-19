from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    idade = Column(Integer, nullable=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"), nullable=True) # nullable=True permite desvincular o tutor

    # Relacionamento com Tutor
    tutor = relationship("Tutor", back_populates="animais")

    # Relacionamento com Consulta
    consultas = relationship("Consulta", back_populates="animal", cascade="all, delete-orphan")

    # Relacionamento com Vacina
    vacinas = relationship("Vacina", back_populates="animal", cascade="all, delete-orphan")