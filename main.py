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

        self.tasks_list = updated_list

        return self.tasks_list
    
    def get_by_priority(self, priority):
        same_priority_list = []

        for current_priority in self.tasks_list:
            if current_priority.priority.lower() == priority.lower():
                same_priority_list.append(current_priority)        
        
        return same_priority_list
    
    def get_by_status(self, status):
        same_status_list = []

        for current_status in self.tasks_list:
            if current_status.status.lower() == status.lower():
                same_status_list.append(current_status)
            
        return same_status_list
    
    def search_tasks(self, search_string):
        same_string_list = []

        for current_task in self.tasks_list:
            if search_string.lower() in current_task.description.lower():
                same_string_list.append(current_task)

        return same_string_list
        

tasks = TaskList("Work Tasks")
tasks.add_task(Task("Fix bug in search", "high", "pending"))
tasks.add_task(Task("Write documentation", "low", "pending"))
tasks.add_task(Task("Review code", "high", "completed"))

print(tasks.get_by_priority("high"))  # Should return 2 tasks (bug fix and review)
print(tasks.search_tasks("bug"))  # Should return 1 task (bug fix)
print(tasks.get_by_status("pending"))  # Should return 2 tasks (bug fix and docs)