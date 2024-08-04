import os

class ToDoList:
def __init__(self):
self.tasks = []

def add_task(self, task):
self.tasks.append(task)
print(f"Task '{task}' added.")

def update_task(self, task_index, new_task):
if 0 <= task_index < len(self.tasks):
old_task = self.tasks[task_index]
self.tasks[task_index] = new_task
print(f"Task '{old_task}' updated to '{new_task}'.")
else:
print("Invalid task index.")

def delete_task(self, task_index):
if 0 <= task_index < len(self.tasks):
removed_task = self.tasks.pop(task_index)
print(f"Task '{removed_task}' deleted.")
else:
print("Invalid task index.")

def view_tasks(self):
if not self.tasks:
print("No tasks in the list.")
else:
print("To-Do List:")
for idx, task in enumerate(self.tasks, 1):
print(f"{idx}. {task}")

def display_menu():
print("\nTo-Do List Application")
print("1. Add task")
print("2. Update task")
print("3. Delete task")
print("4. View tasks")
print("5. Exit")

def main():
todo_list = ToDoList()

while True:
display_menu()
choice = input("Enter your choice (1-5): ")

if choice == '1':
task = input("Enter input here: ")


import os

class SpeakingExperience:
def __init__(self):
self.tasks = []

def add_task(self, task):
self.tasks.append(task)
print(f&q uot;Task '{task}' added.")

def update_task(self, task_index, new_task):
if 0 <= task_index < len(self.tasks):
old_task = self.tasks[task_index]
self.tasks[task_index] = new_task
print("Task '{old_task}' updated to '{new_task}'.")
else:
print("Invalid task index.")

def delete_task(self, task_index):
if 0 <= task_index < len(self.tasks):
removed_task = self.tasks.pop(task_index)
print(f&q uot;Task '{removed_task}' deleted.")
else:
print("Invalid task index")