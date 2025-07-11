import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for idx, task in enumerate(tasks):
        status = "✔" if task["done"] else "✗"
        print(f"{idx + 1}. [{status}] {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == "3":
            idx = int(input("Task number to mark done: ")) - 1
            mark_done(tasks, idx)
        elif choice == "4":
            idx = int(input("Task number to delete: ")) - 1
            delete_task(tasks, idx)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
