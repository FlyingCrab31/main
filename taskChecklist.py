from prettytable import PrettyTable

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = {task["Task"]: task["Status"] for task in tasks} if tasks else {}

    def display_tasks(self):
        table = PrettyTable()
        table.field_names = ["Task", "Status"]
        for task, status in self.tasks.items():
            table.add_row([task, status])
        print(table)

    def mark_task_completed(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name] = "Completed"
            print(f'Task "{task_name}" marked as completed.')
        else:
            print(f'Task "{task_name}" not found.')

    def add_task(self, task_name):
        if task_name not in self.tasks:
            self.tasks[task_name] = "Pending"
            print(f'Task "{task_name}" added.')
        else:
            print(f'Task "{task_name}" already exists.')

    def delete_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f'Task "{task_name}" deleted.')
        else:
            print(f'Task "{task_name}" not found.')


    def menu(self):
        while True:
            print("\n1. View tasks\n2. Add task\n3. Mark task completed\n4. Delete task\n5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task_name = input("Enter task name: ")
                self.add_task(task_name)
            elif choice == '3':
                task_name = input("Enter task name to mark as completed: ")
                self.mark_task_completed(task_name)
            elif choice == '4':
                task_name = input("Enter task name to delete: ")
                self.delete_task(task_name)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tasks_data = [
        {"Task": "Research best practices for integrating multiple modules", "Status": "Pending"},
        {"Task": "Develop integration points between modules", "Status": "Pending"}
    ]

    # Create TaskManager
    task_manager = TaskManager(tasks_data)

    # Call the menu method
    task_manager.menu()

    # Display initial tasks
    print("Initial Task List:")
    task_manager.display_tasks()

    # Delete Task
    task_manager.delete_task("Start implementing basic integration functionalities")

    # Marking a task as completed
    task_manager.mark_task_completed("Develop integration points between various modules")

    # Display updated tasks
    print("\nUpdated Task List:")
    task_manager.display_tasks()

    # Again display Task
    print("\nFinal Task List:")
    task_manager.display_tasks()
