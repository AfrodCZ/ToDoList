from fastapi import FastAPI
from app.logic import Task
from pydantic import BaseModel
from app.storage import save_task, load_tasks, save_all_tasks
from fastapi.responses import JSONResponse

class TaskModel(BaseModel):
    title: str
    description: str
    date: str
    priority: str

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