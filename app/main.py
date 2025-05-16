from datetime import datetime

from app.storage import load_tasks, save_task, Database, save_all_tasks
from logic import Task
import storage

def main():
    while True:
        print("Choose first option\n 1. Add task \n 2. Mark task as Done \n 3. Delete task \n 4. Show all task \n q: Exit")
        choice = input("Choose option: ")
        FILE = "tasks.csv"

        if choice == "1":
            title = input("Create name task: ")
            date = input("Fill you date d-m-Y: ")
            priority = input("Fill priority: ")
            try:
                task_create = Task(title, date, priority, status="New")
                save_task(task_create)
                print("Task was successfully created")
            except Exception as e:
                print(f"Task wasn't created! Error {e}")
        elif choice == "2":
            change_name = input("Write the name of the task for change: ")
            tasks = load_tasks()
            found = False
            for task in tasks:
                if task.title == change_name:
                    task.status = "Done"
                    found = True
                    print("The task marked as done has been changed")
                    break
            if not found:
                print("Task wasn't found")

            save_all_tasks(tasks)
        elif choice == "3":
            delete_task = input("Write task to delete: ")
            tasks = load_tasks()
            tasks1 = [task for task in tasks if task.title != delete_task]
            save_all_tasks(tasks1)
            print("Task was successfully deleted")

        elif choice == "4":
            tasks = load_tasks()
            for task in tasks:
                print(task)

        elif choice == "q":
            break

if __name__ == "__main__":
    main()