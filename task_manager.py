import datetime
import heapq

# Class representing a task
class Task:
    def __init__(self, title, category, priority, due_date):
        # Initialize a task with title, category, priority, and due date
        self.title = title
        self.category = category
        self.priority = priority.capitalize()  # Ensure priority is always capitalized
        self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Pending"
    
    def mark_complete(self):
        # Mark the task as completed
        self.status = "Completed"

    def __lt__(self, other):
        # Compare tasks based on priority and due date for sorting
        priority_order = {"High": 0, "Low": 1}  # Define priority order
        return (priority_order[self.priority], self.due_date) < (priority_order[other.priority], other.due_date)

    def __str__(self):
        # Return a string representation of the task
        return f"{self.title} | {self.category} | {self.priority} | Due: {self.due_date.date()} | Status: {self.status}"

# Class representing the task manager
class TaskManager:
    def __init__(self):
        # Initialize the task manager with some pre-existing tasks
        self.tasks = []
        self.add_task("Submit report", "Work", "High", "2025-02-20")
        self.add_task("Buy groceries", "Personal", "Low", "2025-02-15")
        self.add_task("Doctor's appointment", "Health", "High", "2025-02-18")

    def add_task(self, title, category, priority, due_date):
        # Add a new task to the task manager, accepting both uppercase and lowercase inputs
        priority = priority.capitalize()
        if priority not in ["High", "Low"]:
            print("Invalid priority! Please enter 'High' or 'Low'.\n")
            return
        task = Task(title, category, priority, due_date)
        heapq.heappush(self.tasks, task)
        print(f"Task '{title}' added successfully!\n")

    def remove_task(self, title):
        # Remove a task by title, checking if it exists first
        found = any(task.title == title for task in self.tasks)
        if not found:
            print(f"Task '{title}' not found!\n")
            return
        self.tasks = [task for task in self.tasks if task.title != title]
        heapq.heapify(self.tasks)
        print(f"Task '{title}' removed successfully!\n")

    def update_task_status(self, title):
        # Mark a task as completed by title
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as completed!\n")
                return
        print(f"Task '{title}' not found.\n")

    def show_tasks(self):
        # Display all tasks in the task manager
        if not self.tasks:
            print("No tasks available!\n")
            return
        print("Task List:")
        for task in sorted(self.tasks):
            print(task)
        print()

    def show_tasks_by_category(self, category):
        # Display tasks filtered by category
        filtered_tasks = [task for task in self.tasks if task.category.lower() == category.lower()]
        if not filtered_tasks:
            print(f"No tasks found in category '{category}'.\n")
            return
        print(f"Tasks in category '{category}':")
        for task in sorted(filtered_tasks):
            print(task)
        print()

    def check_due_dates(self):
        # Check for tasks that are due today or overdue and print reminders
        today = datetime.datetime.today().date()
        for task in self.tasks:
            if task.due_date.date() <= today and task.status == "Pending":
                print(f"Reminder: Task '{task.title}' is due today or overdue!\n")

# Main function to run the task manager menu
def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Show All Tasks")
        print("5. Show Tasks by Category")
        print("6. Check Due Dates")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Add a new task
            title = input("Enter task title: ")
            category = input("Enter category: ")
            priority = input("Enter priority (High/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(title, category, priority, due_date)
        
        elif choice == "2":
            # Remove a task
            title = input("Enter task title to remove: ")
            manager.remove_task(title)
        
        elif choice == "3":
            # Mark a task as completed
            title = input("Enter task title to mark as completed: ")
            manager.update_task_status(title)
        
        elif choice == "4":
            # Show all tasks
            manager.show_tasks()
        
        elif choice == "5":
            # Show tasks by category
            category = input("Enter category to filter: ")
            manager.show_tasks_by_category(category)
        
        elif choice == "6":
            # Check due dates for reminders
            manager.check_due_dates()
        
        elif choice == "7":
            # Exit the program
            print("Exiting Task Manager. Have a great day!")
            break
        
        else:
            print("Invalid choice, please try again.\n")

# Entry point for the program
if __name__ == "__main__":
    main()
