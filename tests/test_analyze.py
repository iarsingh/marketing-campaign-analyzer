from fastapi.testclient import TestClient
from campaign.main import app

client = TestClient(app)


def test_summary():
    payload = client.post("/analyze", json={"rows": [{'channel': 'email', 'conversions': 10}, {'channel': 'email', 'conversions': 30}, {'channel': 'ads', 'conversions': 20}]}).json()
    assert payload["mean"] == 20.0
    assert payload["by_channel"]["email"]


def test_empty_is_refused():
    assert client.post("/analyze", json={"rows": []}).status_code == 422
