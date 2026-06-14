#Task menage

from Tasks import add_task,show_tasks

while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Show Task")
    print("3. Exit")


    choice = input("Choose: ")

    if choice == "1":
        task =input("Enter task: ")
        add_task(task)


    elif choice == "2":
        show_tasks()

    elif choice == "3":
        print("Byee!")
        break
    

    else:
        print("Invalid Choice")