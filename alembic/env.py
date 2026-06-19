import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlalchemy import create_engine

# Adiciona o caminho do projeto ao sys.path para o Python encontrar a pasta 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importa a Base e os modelos
from app.core.database import Base
import app.models  # Força o carregamento dos modelos para o Alembic mapear as tabelas

# Configuração do Alembic
config = context.config

# 🔧 Inteligência de ambiente: Lê a URL do contêiner ou cai no padrão interno correto
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:senha@localhost:5432/clinica_db")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata dos modelos
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executa migrations no modo offline (gera SQL sem conectar ao banco)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa migrations no modo online (conectado ao banco)."""
    # Coleta as configurações atualizadas com o set_main_option feito acima
    connectable = engine_from_config(
        config.get_section(config.config_ini_section) or {},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Decide se roda offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()