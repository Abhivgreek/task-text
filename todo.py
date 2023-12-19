# todo.py

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def main():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
