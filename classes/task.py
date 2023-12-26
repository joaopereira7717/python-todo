class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False
    
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} - {self.description} - {self.due_date} - {self.priority} - {status}"

