import time

def add_task(tasks):
    task=input("Enter a task to add: ")
    task=task.capitalize()
    tasks.append(task)

def remove_task(tasks):
    if not tasks:
        print("No tasks exist")
        time.sleep(1)
        return
    task=input("Enter a task to remove: ")
    task=task.capitalize()
    if task not in tasks:
        print("Entered task doesn't exist!")
        time.sleep(1)
    tasks.remove(task)
    print(task,"removed successfully!")

def show_task(tasks):
    if not tasks:
        print("No tasks exist")
        time.sleep(1)
    task_no=len(tasks)
    for i in range(1,task_no+1):
        print("i"*i+") "+tasks[i-1])
    time.sleep(1)
    print("\n\n")
    return
    

def to_do_list():
    tasks=[]
    while True:
        
        print("1. Add task.")
        print("2. Remove task.")
        print("3. Show tasks.")
        print("4. Quit\n")
        choice=(input("Enter a choice(1/2/3/4):"))

        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            remove_task(tasks)
        elif choice=="3":
            show_task(tasks)
        elif choice=="4":
            print("\nThank you\n")
            break
        else:
            print("Enter a valid choice!!!\n")
            time.sleep(1)
            


print("\nWelcome to CLI TO-DO List!!\n")
to_do_list()
