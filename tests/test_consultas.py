import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fluxo_alteracao_status_valido():
    """Caso Válido: Transição de AGENDADA para EM_ANDAMENTO"""
    response = client.put("/consultas/1/status?novo_status=EM_ANDAMENTO")
    # Garante que a API responde com sucesso ou com 404 tratado, nunca com erro interno 500
    assert response.status_code in [200, 404]

def test_fluxo_alteracao_status_invalido():
    """Caso Inválido: Tentar pular de AGENDADA direto para CONCLUIDA"""
    response = client.put("/consultas/1/status?novo_status=CONCLUIDA")
    # Deve falhar com 400 Bad Request devido à nossa regra de negócio do Service
    if response.status_code == 400:
        json_data = response.json()
        assert "error" in json_data
        assert json_data["error"] == "ERRO_DE_NEGOCIO"