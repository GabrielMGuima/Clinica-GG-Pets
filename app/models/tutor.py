from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)

    # Relacionamentos
    animais = relationship("Animal", back_populates="tutor", cascade="all, delete-orphan")
    consultas = relationship("Consulta", back_populates="tutor", cascade="all, delete-orphan")
