import pytest

def test_criar_consulta(client):
    # Primeiro criamos tutor e animal para ter IDs válidos
    tutor = client.post("/tutores/", json={"nome": "T", "email": "t@t.com", "telefone": "123"}).json()
    animal = client.post("/animais/", json={"nome": "Bidu", "especie": "Cachorro", "idade": 2, "tutor_id": tutor["id"]}).json()
    
    response = client.post("/consultas/", json={
        "data": "2026-06-20", 
        "descricao": "Check-up rotina", 
        "tutor_id": tutor["id"], 
        "animal_id": animal["id"]
    })
    assert response.status_code == 201

def test_listar_consultas(client):
    response = client.get("/consultas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_consulta_inexistente(client):
    response = client.get("/consultas/99999")
    assert response.status_code == 404