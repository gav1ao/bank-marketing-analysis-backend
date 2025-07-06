import json

import pytest

from src.app import create_app

app = create_app()


@pytest.fixture
def client():
    """Configura o cliente de teste para a aplicação Flask"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_bank_client_data():
    """Dados de exemplo para teste"""
    return {
        "age": "21",
        "job": "services",
        "marital": "married",
        "education": "secondary",
        "default": "yes",
        "balance": "1000",
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "day": "13",
        "month": "jan",
        "duration": "1",
        "campaign": "1",
        "p_days": "1",
        "previous": "1",
        "p_outcome": "unknown"
    }


def test_docs_redirect(client):
    """Testa se a rota docs redireciona para openapi"""

    response = client.get("/")
    assert response.status_code == 302
    assert "/openapi" in response.location


def test_prediction_success(client, sample_bank_client_data):
    """Testa a predição de adesão ao produto bancário"""

    response = client.post("/predict_offer",
                           data=json.dumps(sample_bank_client_data),
                           content_type="application/json")

    assert response.status_code == 200
    data = json.loads(response.data)

    assert "will_accept_offer" in data
    assert data["will_accept_offer"] in [False, True]
