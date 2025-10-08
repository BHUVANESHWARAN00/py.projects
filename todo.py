tasks=[]
while True:
    print("\n To Do list menu")
    print("1. View task")
    print("2. add new task")
    print("3. remove task")
    print("4. exit")

    choice=input("Enter your number:")
    if choice =="1":
        if not tasks:
            print("no task in your list")
        else:
            print("your task")
            for i in range (len(tasks)):
                print(f"{i+1}.{tasks[i]}")
    elif choice =="2":
        newtask=input("Enter a new task:")
        tasks.append(newtask)
        print("task added succesfully")
    elif choice == "3":
        if not tasks:
            print("no task removed")
        else:
            num=int(input("Enter the number to remove:"))
            if 0 < num < len(tasks):
                tasks.pop(num-1)
                print("task removed sucessfully")
             
            else:
                print("Invalid task")
    elif choice == "4":
        print("Good bye")
    else:
        print("invalid choice!   try again")
  
           
