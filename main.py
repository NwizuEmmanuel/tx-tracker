import json
import argparse
import os
from datetime import datetime
from prettytable import PrettyTable

def load_tasks():
    file_path = "tasks.json"
    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
            data = {"tasks": []}
            json.dump(data, f, indent=4)
    with open(file_path, "r") as f:
        return json.load(f)

def save_task(data):
    with open("tasks.json",'w',encoding="utf-8") as f:
        json.dump(data, f, indent=4)

args = parser.parse_args()

def print_table(tasks):
    table = PrettyTable()
    table.field_names = ["id","description","status","createdAt","updatedAt"]
    for task in tasks:
        table.add_row([
            task["id"],
            task["description"],
            task["status"],
            task["createdAt"],
            task["updatedAt"],
            ])
    print(table)

def add_task():
    tasks = load_tasks()
    count = len(tasks["tasks"]) + 1
    data = {
        "id": count,
        "description": args.add,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now()),
    }
    tasks["tasks"].append(data)
    save_task(tasks)
    print("Task added successfully.")

def update_task():
    tasks = load_tasks() 
    for task in tasks["tasks"]:
        if task["id"] == int(args.update[0]):
            task["description"] = args.update[1]
    save_task(tasks)
    print("Task is updated")

def delete_task():
    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == args.delete:
            tasks["tasks"].remove(task)     
    save_task(tasks)
    print("Task deleted.")

def list_tasks():
    tasks = load_tasks()["tasks"]
    print_table(tasks)

def mark_in_progress():
    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == args.mark_in_progress:
            task["status"] = "in_progress"
            task["updatedAt"] = str(datetime.now())
    save_task(tasks)
    print("Task marked in progress.")


def mark_done():
    tasks = load_tasks()
    for task in tasks["tasks"]:
        if task["id"] == args.mark_done:
            task["status"] = "done"
            task["updatedAt"] = str(datetime.now())
    save_task(tasks)
    print("Task marked done.")

def list_tasks_done():
    tasks = load_tasks()
    done_tasks = [task for task in tasks["tasks"] if task["status"] == "done"]
    print_table(done_tasks)     
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a CLI app for tracking task.")
    parser.add_argument("-a", "--add", type=str, help="To add new task.")
    parser.add_argument("-u", "--update", nargs="+", help="To update existing task.")
    parser.add_argument("-d", "--delete", type=int, help="To delete a task.")
    parser.add_argument("-mp", "--mark-in-progress", type=int, help="To mark a task in progress.")
    parser.add_argument("-md", "--mark-done", type=int, help="To mark a task done.")
    parser.add_argument("-l", "--list", action="store_true", help="To list all task.")
    parser.add_argument("-ld", "--list-done", action="store_true", help="To list done task only.")
    parser.add_argument("-lt", "--list-todo", action="store_true", help="To list todo task only.")
    parser.add_argument("-lp", "--list-in-progress", action="store_true", help="To list in-progress task only.")

    if args.add:
        add_task()   
    elif args.list:
        list_tasks()
    elif args.update:
        update_task()
    elif args.delete:
        delete_task() 
    elif args.mark_in_progress:
        mark_in_progress()  
    elif args.mark_done:
        mark_done()
    elif args.list_done:
        list_tasks_done() 