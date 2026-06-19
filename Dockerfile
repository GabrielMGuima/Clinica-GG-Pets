FROM python:3.9-slim

# Define a pasta onde o volume local vai se acoplar
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala os pacotes antes de copiar o código (otimiza o tempo de build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a estrutura exata do seu projeto para o contêiner
COPY . .

EXPOSE 8000

# 🔴 O COMANDO DEFINITIVO:
# Usamos o caminho absoluto "app.main:app" e fixamos o diretório de execução na raiz "/app".
# Isso casa perfeitamente com os imports "from app.database import ..." de todos os seus arquivos.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "/app", "--reload"]