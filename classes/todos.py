class ToDoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)
    
    def delete_todo_by_index(self, index):
        self.todos.pop(index)
    
    def update_todo_by_index(self, index, todo):
        status = self.todos[index].completed
        todo.completed = status
        self.todos[index] = todo
    
    def get_all_todos(self):
        return self.todos
    
    def get_todo_by_index(self, index):
        return self.todos[index]

    def sort_todos(self, sort_key):
        self.todos.sort(key=lambda x: getattr(x, sort_key))
        
