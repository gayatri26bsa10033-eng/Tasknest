#TO-DO LIST PROJECT

tasks = []
while True:
    print("\n===== TO-DO LIST=====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Progress check")
    print("6. Exit")

    choice = input("Enter your choice(1-6): ")

    
    if choice =="1":
        task = input("Enter your task: ")
        print("select Priority (High/Medium/Low): ")
        priority = input("Enter priority: ")
        tasks.append({"task": task, "completed": False, "priority": priority})
        print("Task added successfully!")

    
    elif choice =="2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n-----YOUR TASKS-----")
            for i,item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"] else "Pending"
                print(f"{i}. {item['task']} - {status}-Priority:{item['priority']}")

    
    elif choice =="3":
        if len(tasks) ==0:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"]else "Pending"
                print(f"{i}. {item['task']} - {status}-Priority:{item['priority']}")
        try:
            task_num = int(input("Enter the task number to mark as completed:"))
            if 1<= task_num <= len(tasks):
                tasks[task_num -1]["completed"]= True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice =="4":
        if len(tasks) ==0:
            print("No tasks available.")
        else:
            for i, item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"]else "Pending"
                print(f"{i}. {item['task']} - {status}-Priority:{item['priority']}")

            try:
                task_num = int(input("Enter the task number to delete:"))
                if 1<= task_num <= len(tasks):
                    del tasks[task_num -1]
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    
    elif choice =="5":
        if len(tasks) ==0:
            print("No tasks available.")
        else:
            completed_tasks = sum(1 for task in tasks if task["completed"])
            total_tasks = len(tasks)
            pending_tasks = total_tasks - completed_tasks
            percentage_completed = (completed_tasks / total_tasks) *100
            print(f"\n-----PROGRESS CHECK-----")
            print(f"Total tasks: {total_tasks}")
            print(f"Completed tasks: {completed_tasks}")
            print(f"Pending tasks: {pending_tasks}")
            print(f"Completion percentage: {percentage_completed:.1f}%")
        if pending_tasks == 0:
            print("🎉Amazing! All tasks completed!")
        elif completed_tasks > 0:
            print("💪🏻Great job! keep going!")
        else:
            print("😅You have a lot of work to do!")


    elif choice == "6":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

