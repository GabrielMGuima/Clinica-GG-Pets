from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class Vacina(Base):
    __tablename__ = "vacinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_aplicacao = Column(Date, nullable=False)
    animal_id = Column(Integer, ForeignKey("animais.id"))

    # Relacionamento com Animal
    animal = relationship("Animal", back_populates="vacinas")
