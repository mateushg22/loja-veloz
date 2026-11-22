from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_ready():
    client = app.test_client()
    response = client.get("/ready")
    assert response.status_code == 200


def test_create_and_list_orders():
    client = app.test_client()
    post_resp = client.post(
        "/orders",
        json={"customer": "Ana", "sku": "SKU-1", "quantity": 2, "amount": 149.90},
    )
    assert post_resp.status_code == 201
    data = post_resp.get_json()
    assert data["order"]["customer"] == "Ana"

    get_resp = client.get("/orders")
    assert get_resp.status_code == 200
    assert get_resp.get_json()["total"] >= 2
