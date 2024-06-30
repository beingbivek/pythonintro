# Create program to ask user to enter n no. of todo and display it
todos = []

total_todo = int(input("Enter total number of todo: "))

for i in range(1,total_todo +1):
    todo = input(f"Enter Todo {i}: ")
    todos.append(todo)

print("\n---------\n")
print("All todos are:")
for todo in todos:
    print(todo)