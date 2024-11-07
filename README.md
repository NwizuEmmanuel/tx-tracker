# tx-tracker
A command line tool for tracking task.
https://roadmap.sh/projects/task-tracker

# How to install
## step 1
Clone this project.
```
git clone https://github.com/NwizuEmmanuel/tx-tracker.git
```
## step 2
Install required packages
```
pip install -r requirements.txt
```

# How to use
Firstly change your directory to main.py directory.<br>
1. To add new task.
```
py main.py --add "Todo 1"
```
2. To update task
```
py main.py --update 1 "new task"
```
3. To list all tasks
```
py main.py --list
```
4. To delete task
```
py main.py --delete 1
```
5. To mark task done
```
py main.py --mark-done 1
```
6. To mark task in-progress
```
py main.py --mark-in-progress
```
7. To list task done only
```
py main.py --list-done
```
8. To list task in-progress only
```
py main.py --list-in-progress
```
9. To list todo tasks only
```
py main.py --list-todo
```
## *Note:*
You replace main.py with the app name(tx-tracker) after building the app.
10. To view more about the app.
```
py main.py --help
```
or
```
py main.py -h
```

## Thanks 😊