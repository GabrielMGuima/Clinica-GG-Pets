import pytest
from fastapi.testclient import TestClient

def test_criar_tutor(client):
    response = client.post("/tutores/", json={"nome": "Carlos", "email": "carlos@teste.com", "telefone": "123456789"})
    assert response.status_code == 201

def test_email_duplicado(client):
    client.post("/tutores/", json={"nome": "B", "email": "duplicado@teste.com", "telefone": "000000000"})
    response = client.post("/tutores/", json={"nome": "B", "email": "duplicado@teste.com", "telefone": "000000000"})
    assert response.status_code in [400, 422]

def test_buscar_tutor_nao_encontrado(client):
    response = client.get("/tutores/99999")
    assert response.status_code == 404