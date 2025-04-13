import csv
from dataclasses import field
from operator import delitem
from logic import Task

def save_task():
    ...

def export_task(task, filename="tasks.csv"):
    with open(filename,'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile )
        writer.writerow(task.to_list())

def load_tasks(filename="tasks.csv"):
    tasks = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task = Task(
                 title = row['title'],
                 date = row['date'],
                 priority = row['priority']
            )
            task.status = row['status']
            tasks.append(task)
    return tasks

class Tools:
 pass



