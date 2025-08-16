class TodoManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['description']}")

    def add_task(self, description):
        if description:
            self.tasks.append({"description": description, "completed": False})
            print("Task added successfully!")
        else:
            print("Task description cannot be empty.")

    def complete_task(self, task_num):
        try:
            task_num = int(task_num)
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num-1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self, task_num):
        try:
            task_num = int(task_num)
            if 1 <= task_num <= len(self.tasks):
                deleted_task = self.tasks.pop(task_num-1)
                print(f"Deleted task: {deleted_task['description']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")