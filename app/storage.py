import csv
import sqlite3
from dataclasses import field
from operator import delitem
from logic import Task
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
        self.cursor.execute('SELECT title, date, priority, status')
        self.cursor.fetchall()

    def close(self):
        self.conn.close()


# export tasku do CSV
def export_task(task, filename="tasks.csv"):
    with open(filename,'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile )
        writer.writerow(task.to_list())

# nahrání CSV
def load_tasks(filename="tasks.csv"):
    tasks = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(
                 title = row['title'],
                 date = row['date'],
                 priority = row['priority'],
                status = row['status']
            )
            tasks.append(task)
    return tasks
# import z CSV do DB


# různé nástroje pro práci s tasky
class Tools:
 pass



