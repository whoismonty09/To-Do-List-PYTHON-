tasks = []

def show_menu():
    print("\n TO DO list developed by Monty")
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("2.Exit")

while True:
    show_menu() 
    choice = input("Enter your choice(1-4): ")

    if choice == "1": 
        task = input("Enter task: ") 
        tasks.append(task) 
        print("Task added successfully!")

    elif choice == "2":
        if not task:
            print("No task available0") 
        else:
            print("\n Your tasks")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not task:
            print("No task to delete")
        else: 
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Good Byee!")  
        break 

    else:
        print("Invalide choice Please try again")        
               
