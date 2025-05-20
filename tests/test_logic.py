from app.logic import Task

def test_create_task():
    task = Task("Test", "Popis", "2025-01-01", "Vysoká")
    assert task.title == "Test"
    assert task.description == "Popis"
    assert task.date == "2025-01-01"
    assert task.priority == "Vysoká"
    assert task.status == "New"
