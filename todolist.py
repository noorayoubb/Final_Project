import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    task_description = input("Enter the task description: ")
    priority = input("Enter the task priority (High, Medium, Low): ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    tasks.append({"description": task_description, "priority": priority, "due_date": due_date})
    print("Task added.")

def remove_task(tasks):
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task removed.")
    else:
        print("Invalid task number.")

def view_tasks(tasks):
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['description']} - Priority: {task['priority']}, Due: {task['due_date']}")

def modify_task(tasks):
    task_index = int(input("Enter the task number to modify: ")) - 1
    if 0 <= task_index < len(tasks):
        new_description = input("Enter the new description (leave blank to keep current): ")
        new_priority = input("Enter the new priority (High, Medium, Low; leave blank to keep current): ")
        new_due_date = input("Enter the new due date (YYYY-MM-DD; leave blank to keep current): ")

        if new_description:
            tasks[task_index]["description"] = new_description
        if new_priority:
            tasks[task_index]["priority"] = new_priority
        if new_due_date:
            tasks[task_index]["due_date"] = new_due_date

        print("Task modified.")
    else:
        print("Invalid task number.")

# New function to sort tasks by their due date
def sort_tasks(tasks):
    return sorted(tasks, key=lambda task: task['due_date'])

def main():
    tasks = load_tasks()  # Load tasks from file

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Modify Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            tasks_sorted = sort_tasks(tasks)
            view_tasks(tasks_sorted)
        elif choice == '4':
            modify_task(tasks)
        elif choice == '5':
            save_tasks(tasks)  # Save tasks to file
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()