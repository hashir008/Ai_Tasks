tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")
    print()

while True:
    print("==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        title = input("Enter task: ")
        tasks.append({"title": title, "done": False})
        print("Task added.\n")
    
    elif choice == "2":
        show_tasks()
    
    elif choice == "3":
        show_tasks()
        if tasks:
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["done"] = True
                print("Marked complete.\n")
            else:
                print("Invalid number.\n")
    
    elif choice == "4":
        show_tasks()
        if tasks:
            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                print("Deleted.\n")
            else:
                print("Invalid number.\n")
    
    elif choice == "5":
        print("Goodbye.")
        break
    
    else:
        print("Invalid choice.\n")
