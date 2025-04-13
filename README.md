# To-Do List with Priorities, Deadlines, and Simple API

### What is this?

This is a small application for organizing your time and tasks, written in Python.

- Add tasks
- Set deadlines and priorities
- View tasks by priority or deadline
- Mark tasks as done
- Save tasks to SQLite
- Export tasks to CSV
- Includes a simple API for frontend or mobile apps

### Unit tests in the app:

- Adding a task
- Marking a task as done
- Filtering by priority or deadline
- Saving and loading tasks

---

## Reauirements

- Python 3.10+
- pip

Install required packages:

pip instal -r requirements.txt

## How to run

Start the FastAPI server (backend)

uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

You can try it using the built-in docs:
http://127.0.0.1:8000/docs

## How to start Unit tests

python -m unittest doscover tests