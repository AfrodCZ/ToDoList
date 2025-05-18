# To-Do List with Priorities, Deadlines, and Simple API

### What is this?

This is a small application for organizing your time and tasks, written in Python for CLI.

- Add tasks
- Set deadlines and priorities
- View all tasks
- Mark tasks as done
- Save tasks to SQLite
- Export tasks to CSV
- Includes a simple API for frontend

### Unit tests in the app:

- Adding a task
- Marking a task as done
- Showing all tasks
- Saving and loading tasks

---

## Reauirements

- Python 3.12+
- pip

Install required packages:

pip install -r requirements.txt

## How to start App
python -m app.main

## How to run API

Start the FastAPI server (backend)

uvicorn app.fapi:app --reload

The API will be available at:
http://127.0.0.1:8000

You can try it using the built-in docs:
http://127.0.0.1:8000/docs

## How to start Unit tests

python -m unittest doscover tests