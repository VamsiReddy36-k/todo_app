import json
import os

TODO_FILE = "todo_data.json"

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []