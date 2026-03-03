from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def mark_undone(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = False
        save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
