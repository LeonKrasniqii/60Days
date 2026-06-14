from Storage import tasks

def add_task(task):
    tasks.append(task)
    print("Task added")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")

        
