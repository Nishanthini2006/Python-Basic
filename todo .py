tasks = []

def add_task():
    task = input("Enter task: ")
    if task.strip() == "":
        print("Task cannot be empty")
    else:
        tasks.append(task)
        print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        print("\n--- Your Todo List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    try:
        show_tasks()
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number")

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
