todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("===========================")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter your new task: ")
    if task.strip():
        todo_list.append(task)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def update_task():
    view_tasks()
    if not todo_list:
        return
    task_no_input = input("Enter the number of the task to update: ")
    if task_no_input.isdigit():
        task_no = int(task_no_input)
        if 1 <= task_no <= len(todo_list):
            new_task = input("Enter the new task: ")
            if new_task.strip():
                todo_list[task_no - 1] = new_task
                print("Task updated!")
            else:
                print("New task cannot be empty.")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not todo_list:
        return
    task_no_input = input("Enter the number of the task to delete: ")
    if task_no_input.isdigit():
        task_no = int(task_no_input)
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed}' deleted!")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! 👋")
        break
    else:
        print("Please choose a valid option.")
