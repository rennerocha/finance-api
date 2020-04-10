def test_paypal_gateway_accept_request(client):
    response = client.get("/gateway/paypal")
    assert response.status_code == 200


def test_paypal_gateway_content(client):
    response = client.get("/gateway/paypal")
    assert response.json() == {"gateway": "paypal"}
