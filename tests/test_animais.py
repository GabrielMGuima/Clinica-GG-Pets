import pytest
from fastapi.testclient import TestClient


def test_criar_animal(client):
    # Cria o tutor primeiro
    tutor_resp = client.post("/tutores/", json={"nome": "T", "email": "t@t.com", "telefone": "123"})
    tutor_id = tutor_resp.json()["id"]

    # Cria o animal usando o ID real
    response = client.post(
    "/animais/", 
    json={
        "nome": "Bidu", 
        "especie": "Cachorro", 
        "idade": 2,           
        "tutor_id": tutor_id   
    }
    )

    if response.status_code == 422:
            print(f"\nERRO DE VALIDAÇÃO: {response.json()}")
            
    assert response.status_code == 201