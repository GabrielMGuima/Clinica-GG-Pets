import pytest

def test_criar_vacina(client):
    # Primeiro criamos tutor e animal para ter IDs válidos
    tutor = client.post("/tutores/", json={"nome": "T", "email": "t2@t.com", "telefone": "123"}).json()
    animal = client.post("/animais/", json={"nome": "Bidu", "especie": "Cachorro", "idade": 2, "tutor_id": tutor["id"]}).json()
    
    response = client.post("/vacinas/", json={
        "nome": "Vacina V10", 
        "data_aplicacao": "2026-06-20", 
        "lote": "ABC123", 
        "animal_id": animal["id"]
    })
    assert response.status_code == 201

def test_listar_vacinas(client):
    response = client.get("/vacinas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_deletar_vacina(client):
    # Primeiro criamos a vacina
    tutor = client.post("/tutores/", json={"nome": "T3", "email": "t3@t.com", "telefone": "123"}).json()
    animal = client.post("/animais/", json={"nome": "B", "especie": "Gato", "idade": 1, "tutor_id": tutor["id"]}).json()
    vacina = client.post("/vacinas/", json={"nome": "Antirrábica", "data_aplicacao": "2026-06-20", "animal_id": animal["id"]}).json()
    
    # Deleta
    response = client.delete(f"/vacinas/{vacina['id']}")
    assert response.status_code == 204