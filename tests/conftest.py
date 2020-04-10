import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def app() -> FastAPI:
    from finance_api.main import get_application
    app = get_application()
    return app


@pytest.fixture
def client(app) -> TestClient:
    return TestClient(app)