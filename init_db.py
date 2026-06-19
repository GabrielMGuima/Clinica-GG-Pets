from app.core.database import engine, Base
# Importe todos os modelos aqui para o SQLAlchemy reconhecê-los
from app.models.tutor import Tutor
from app.models.animal import Animal  # Adicione esta linha
from app.models.consulta import Consulta  # Adicione esta linha
from app.models.vacina import Vacina  # Adicione esta linha

print("Criando todas as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Sucesso! Todas as tabelas foram criadas.")