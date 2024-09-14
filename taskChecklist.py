
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


tasks_data = [
    {"Task": "Research best practices for integrating multiple modules and ensuring a cohesive user experience.", "Status": "Pending"},
    {"Task": "Develop integration points between various modules", "Status": "Pending"},
    {"Task": "Start implementing basic integration functionalities", "Status": "Pending"}
]


task_manager = TaskManager(tasks_data)

# Display initial tasks
print("Initial Task List:")
task_manager.display_tasks()

#Delete Task
task_manager.delete_task("Start implementing basic integration functionalities")

# Marking a task as completed
task_manager.mark_task_completed("Develop integration points between various modules")

# Display updated tasks
print("\nUpdated Task List:")
task_manager.display_tasks()

# Again display Task
print("\nFinal Task List:")
task_manager.display_tasks()
