import csv
import sqlite3
from csv import DictWriter
from dataclasses import field
from operator import delitem
from app.logic import Task
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "tasks.csv"

# veškeré operace s databází, konstruktor pro sestavení a ověření, zda existuje DB
# vymyslet, jak jednotlivé funkce volat z programu
class Database:
    def __init__(self,  db_name='ToDoList.sqlite'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT, date TEXT, priority TEXT, status TEXT)')

    def add_to_db(self, task):
        ...

    def edit_in_db(self, task):
        ...

    def delete_from_db(self, task):
        ...

    def get_all_task(self):
        self.cursor.execute('SELECT title, description, date, priority, status')
        self.cursor.fetchall()

    def close(self):
        self.conn.close()

# export tasku do CSV
def save_task(task, filename=CSV_PATH, encoding='utf-8'):
    file_exists = os.path.exists(filename)
    write_header = not file_exists or os.stat(filename).st_size == 0

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description', 'date', 'priority', 'status']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(task.to_dict())

# nahrání CSV
def load_tasks(filename=CSV_PATH, encoding='utf-8'):
    tasks = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(
                 title = row['title'],
                 description = row['description'],
                 date = row['date'],
                 priority = row['priority'],
                 status = row['status']
            )
            tasks.append(task)
    return tasks
#pomocná funkce pro uložení změněných hodnot

def save_all_tasks(tasks, filename=CSV_PATH):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["title", "description", "date", "priority", "status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "title": task.title,
                "description": task.description,
                "date": task.date,
                "priority": task.priority,
                "status": task.status
            })



# import z CSV do DB


# různé nástroje pro práci s tasky
class Tools:
 pass



