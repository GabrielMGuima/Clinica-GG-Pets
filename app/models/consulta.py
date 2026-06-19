from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    descricao = Column(String, nullable=False)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))
    animal_id = Column(Integer, ForeignKey("animais.id"))

    tutor = relationship("Tutor", back_populates="consultas")
    animal = relationship("Animal", back_populates="consultas")