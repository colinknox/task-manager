class Task:
    def __init__(self, description, priority, status):
        self.description = description
        self.priority = priority
        self.status = status

class TaskList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.tasks_list = []

    def add_task(self, task):
        self.tasks_list.append(task)

    def remove_task(self, task):
        updated_list = []
        for current_task in self.tasks_list:
            if current_task.description.lower() != task.description.lower():
                updated_list.append(current_task)

        return updated_list


task_one = Task("Get a gallon of milk", "High", "Pending")
task_two = Task("Chew gum", "Medium", "Completed")
grocery_list = TaskList("Grocery List")

# print(f"BEFORE CURRENT ITEMS IN TASKS LIST: {grocery_list.tasks_list}")
grocery_list.add_task(task_one)
grocery_list.add_task(task_two)
print(f"BEFORE CURRENT ITEMS IN TASKS LIST: {grocery_list.tasks_list}")
print(grocery_list.remove_task(task_one))
