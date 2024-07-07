# WAP to ask user to enter todos and print all todos

total_todo = int(input("Enter no of todo's: "))
todos = []

# Ask User
for i in range(total_todo):
    todo = input(f"Enter Todo {i+1}: ")
    todos.append(todo)

# Print all todos
for todo in todos:
    print(todo)