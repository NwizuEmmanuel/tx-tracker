import json, argparse
import os
from datetime import datetime
from prettytable import PrettyTable

file_path = "tasks.json"
with open(file_path, "a") as f:
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        data = {"tasks": []}
        json.dump(data, f, indent=4)

parser = argparse.ArgumentParser(description="This is a CLI app for tracking task.")
parser.add_argument("-a", "--add", type=str, help="To add new task.")
parser.add_argument("-u", "--update", type=int, help="To update existing task.")
parser.add_argument("-d", "--delete", type=int, help="To delete a task.")
parser.add_argument("-mp", "--mark-in-progress", type=int, help="To mark a task in progress.")
parser.add_argument("-md", "--mark-done", type=int, help="To mark a task done.")
parser.add_argument("-l", "--list", action="store_true", help="To list all task.")
parser.add_argument("-ld", "--list-done", action="store_true", help="To list done task only.")
parser.add_argument("-lt", "--list-todo", action="store_true", help="To list todo task only.")
parser.add_argument("-lp", "--list-in-progress", action="store_true", help="To list in-progress task only.")

args = parser.parse_args()

def app():
    if args.add:
        with open(file_path, "r") as f:
            tasks = json.load(f)

        count = len(tasks["tasks"]) + 1
        data = {
            "id": count,
            "description": args.add,
            "status": "todo",
            "createdAt": str(datetime.now()),
            "updatedAt": str(datetime.now()),
        }
        tasks["tasks"].append(data)
        with open(file_path, "w") as f:
            json.dump(tasks, f, indent=4)
            
    if args.list:
        with open(file_path, "r") as f:
            tasks = json.load(f)["tasks"]
        
        table = PrettyTable()
        table.field_names = ["id","desc","status","createdAt","updatedAt"]
        for task in tasks:
            table.add_row([task["id"],task["description"],task["status"],task["createdAt"],task["updatedAt"]])
        print(table)
    
    if args.update:
        with open(file_path,"r") as f:
            tasks = json.load(f)["tasks"]
        
        
    
if __name__ == "__main__":
    app() 