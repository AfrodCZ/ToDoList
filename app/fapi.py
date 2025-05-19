from fastapi import FastAPI
from app.logic import Task
from pydantic import BaseModel
from app.storage import save_task, load_tasks, save_all_tasks
from fastapi.responses import JSONResponse
from typing import Optional

class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    date: Optional[str] = None
    priority: Optional[str] = None

app = FastAPI()

@app.get("/tasks")
def get_all_tasks():
    tasks = [t.to_dict() for t in load_tasks() ]
    return JSONResponse(content=tasks, media_type="application/json; charset=utf-8")

@app.post("/add")
def post_task(task: TaskModel):
    task_create = Task(
        title=task.title,
        description = task.description,
        date = task.date,
        priority = task.priority,
        status = "New"
    )
    save_task(task_create, filename="app/tasks.csv")
    return {"message": "Task saved", "task": task_create.to_dict()}

@app.put("/update")
def put_task(task: TaskModel):
    tasks = load_tasks(filename="app/tasks.csv")
    updated = False

    for t in tasks:
        if t.title == task.title:
            t.status = "Done"
            updated = True
            break

    if updated:
        save_all_tasks(tasks, filename="app/tasks.csv")
        return {"message": f"Úkol '{task.title}' označen jako hotový."}
    else:
        return {"error": f"Úkol '{task.title}' nebyl nalezen."}