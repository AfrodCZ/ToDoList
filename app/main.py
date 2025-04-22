from datetime import datetime

from app.storage import load_tasks, export_task, Database
from logic import Task
import storage

def main():

    print("Welcome to Your Personal To Do List")
    while True:
        print("Choose first option\n 1. Add task \n 2. Mark task as Done \n 3. Delete task \n 4. Show all task ")
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Create name task: ")
            date = input("Fill you date d-m-Y: ")
            priority = input("Fill priority: ")
            try:
                task_create = Task(title, date, priority)
                export_task(task_create)
                print("Task was successfully created")
            except Exception as e:
                print(f"Task wasn't created! Error {e}")

        elif choice == "4":
            tasks = load_tasks()
            for task in tasks:
                print(task)

if __name__ == "__main__":
    main()