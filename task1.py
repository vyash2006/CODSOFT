import os

FILENAME = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                task, status = line.strip().split("||")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for t in tasks:
            status = "done" if t["done"] else "pending"
            file.write(f"{t['task']}||{status}\n")

def display_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet!")
    else:
        print("\n📋 Your To-Do List:")
        for i, t in enumerate(tasks, 1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {t['task']} [{status}]")
    input("\nPress Enter to continue...")

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("✅ Task added!")
    else:
        print("⚠️ Empty task not added.")
    input("\nPress Enter to continue...")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("☑️ Task marked as done!")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    input("\nPress Enter to continue...")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            print(f"🗑️ Deleted task: {deleted['task']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    input("\nPress Enter to continue...")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("📁 Tasks saved. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
