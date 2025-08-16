from todo_manager import TodoManager
from storage import save_tasks, load_tasks

def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    manager = TodoManager(load_tasks())
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            manager.display_tasks()
        elif choice == "2":
            description = input("Enter task description: ").strip()
            manager.add_task(description)
        elif choice == "3":
            manager.display_tasks()
            task_num = input("Enter task number to complete: ")
            manager.complete_task(task_num)
        elif choice == "4":
            manager.display_tasks()
            task_num = input("Enter task number to delete: ")
            manager.delete_task(task_num)
        elif choice == "5":
            save_tasks(manager.tasks)
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()