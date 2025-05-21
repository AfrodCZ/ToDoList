from app.logic import Task

def test_create_task():
    task = Task("Test", "Desc", "01.12.2025", "High")
    assert task.title == "Test"
    assert task.description == "Desc"
    assert task.date == "01.12.2025"
    assert task.priority == "High"
    assert task.status == "New"
