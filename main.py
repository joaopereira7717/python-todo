import argparse
import pickle
from classes.todos import ToDoList
from classes.task import Task

def save_ToDos(todo_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(todo_list.todos, file)

def load_ToDos(filename):
    try:
        with open(filename, 'rb') as file:
            ToDos = pickle.load(file)
            return ToDos
    except FileNotFoundError:
        return []

def main():
    parser = argparse.ArgumentParser(description="To-Do List App")
    parser.add_argument('--file', default='ToDos.pkl', help='File to save/load ToDos')

    args = parser.parse_args()

    todo_list = ToDoList()
    todo_list.todos = load_ToDos(args.file)

    while True:
        print("\n1. Add ToDo")
        print("2. Update ToDo")
        print("3. Delete ToDo")
        print("4. Sort ToDos")
        print("5. Mark ToDo as Complete")
        print("6. Show ToDos")
        print("7. Save and Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter ToDo title: ")
            description = input("Enter ToDo description: ")
            priority = input("Enter ToDo priority: ")
            due_date = input("Enter ToDo due date: ")
            new_ToDo = Task(title, description, priority, due_date)
            todo_list.add_todo(new_ToDo)

        elif choice == '2':
            index = int(input("Enter ToDo index to update: "))
            title = input("Enter ToDo title: ")
            description = input("Enter ToDo description: ")
            priority = input("Enter ToDo priority: ")
            due_date = input("Enter ToDo due date: ")
            updated_ToDo = ToDo(title, description, priority, due_date)
            todo_list.update_todo_by_index(index, updated_ToDo)

        elif choice == '3':
            index = int(input("Enter ToDo index to delete: "))
            todo_list.delete_todo_by_index(index)

        elif choice == '4':
            sort_key = input("Sort ToDos by (title/priority/due_date): ")
            todo_list.sort_todos(sort_key)

        elif choice == '5':
            index = int(input("Enter ToDo index to mark as complete: "))
            todo_list.todos[index].completed = True

        elif choice == '6':
            for i, ToDo in enumerate(todo_list.todos):
                print(f"{i}. {ToDo}")

        elif choice == '7':
            save_ToDos(todo_list, args.file)
            print("ToDos saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
