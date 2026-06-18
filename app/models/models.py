from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class Tutor(Base):
    __tablename__ = "tutores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)

    animais = relationship("Animal", back_populates="tutor")

class Animal(Base):
    __tablename__ = "animais"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id", ondelete="CASCADE"), nullable=False)

    tutor = relationship("Tutor", back_populates="animais")
    consultas = relationship("Consulta", back_populates="animal")
    vacinas = relationship("Vacina", back_populates="animal")

class Consulta(Base):
    __tablename__ = "consultas"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=False)
    status = Column(String, default="agendada")
    animal_id = Column(Integer, ForeignKey("animais.id", ondelete="CASCADE"), nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id", ondelete="CASCADE"), nullable=False)

    animal = relationship("Animal", back_populates="consultas")
    tutor = relationship("Tutor")

class Vacina(Base):
    __tablename__ = "vacinas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_aplicacao = Column(DateTime, nullable=False)
    animal_id = Column(Integer, ForeignKey("animais.id", ondelete="CASCADE"), nullable=False)

    animal = relationship("Animal", back_populates="vacinas")
