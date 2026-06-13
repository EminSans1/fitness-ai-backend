import sys
import os

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calories_basic():
    response = client.post("/calories", json={
        "weight": 70,
        "duration": 60,
        "intensity": 3,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["weight"] == 70
    assert data["duration"] == 60
    assert data["intensity"] == 3
    assert data["calories_burned"] == 1500.0


def test_calories_short_workout():
    response = client.post("/calories", json={
        "weight": 80,
        "duration": 30,
        "intensity": 2,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["calories_burned"] == 500.0


def test_calories_invalid_intensity():
    response = client.post("/calories", json={
        "weight": 70,
        "duration": 60,
        "intensity": 10,
    })
    assert response.status_code == 422


def test_calories_missing_field():
    response = client.post("/calories", json={"weight": 70})
    assert response.status_code == 422


def test_heart_rate():
    response = client.post("/heart-rate", json={
        "age": 30,
        "resting_hr": 65,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["max_hr"] == 190
    assert data["target_zone_min"] == 114
    assert data["target_zone_max"] == 152


def test_heart_rate_young():
    response = client.post("/heart-rate", json={
        "age": 20,
        "resting_hr": 60,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["max_hr"] == 200


def test_bmr_male():
    response = client.post("/bmr", json={
        "weight": 80,
        "height": 180,
        "age": 25,
        "gender": "male",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["gender"] == "male"
    assert data["bmr"] > 0


def test_bmr_female():
    response = client.post("/bmr", json={
        "weight": 60,
        "height": 165,
        "age": 25,
        "gender": "female",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["gender"] == "female"
    assert data["bmr"] > 0


def test_bmr_invalid_gender():
    response = client.post("/bmr", json={
        "weight": 70,
        "height": 175,
        "age": 30,
        "gender": "other",
    })
    assert response.status_code == 422
