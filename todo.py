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
        return
    for idx, task in enumerate(tasks):
        status = "✔" if task["done"] else "✗"
        due = task.get("due_date", "No due date")
        priority = task.get("priority", "Normal")
        print(f"{idx + 1}. [{status}] {task['title']} (Due: {due}) [Priority: {priority}]")


def add_task(tasks, title, due_date, priority):
    tasks.append({
        "title": title,
        "done": False,
        "due_date": due_date,
        "priority": priority
    })
    save_tasks(tasks)

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def search_tasks(tasks, keyword):
    found = [task for task in tasks if keyword.lower() in task["title"].lower()]
    show_tasks(found)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Mark Done\n4. Delete Task\n5. Search Task\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            due_date = input("Enter due date (e.g., 2025-07-15): ")
            priority = input("Enter priority (High, Medium, Low): ")
            add_task(tasks, title, due_date, priority)

        elif choice == "3":
            idx = int(input("Task number to mark done: ")) - 1
            mark_done(tasks, idx)
        elif choice == "4":
            idx = int(input("Task number to delete: ")) - 1
            delete_task(tasks, idx)
        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
