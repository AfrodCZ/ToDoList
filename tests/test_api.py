from fastapi.testclient import TestClient
from api.todo_api import app
from app.storage import save_all_tasks
from app.logic import Task

client = TestClient(app)

def test_update_task_status():

    task = Task("Test Úkol", "Popis", "2025-06-01", "Střední")
    save_all_tasks([task])  # uloží jeden task do CSV

    response = client.put("/update", json={"title": "Test Úkol"})

    assert response.status_code == 200
    assert "označen jako hotový" in response.json()["message"]
