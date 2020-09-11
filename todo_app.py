def options():
    message = """
    Press 1 to add a task
    Press 2 to delete a task
    Press 3 to view all tasks
    Press q to quit
    """
    print(message)
    answer = input(" ")
    return answer

tasks = []
response = options()
while response != "q":
    if response == "1":
        title = (input("Input the name of the task: ")).upper()
        priority = input("Select priority - Low, Medium, or High: ").upper()
        current_task = {}
        current_task["title"] = title
        current_task["priority"] = priority
        tasks.append(current_task)       
    if response == "2":
        for i in range(0, len(tasks)):
            name_of_task = tasks[i]["title"]
            print(f"{i}-{name_of_task}")
        print(f"{len(tasks)}-Return to menu")
        delete_answer = int(input("Choose number to delete: "))
        if delete_answer in range(0,len(tasks)):
            tasks.pop(delete_answer)
        else:
            pass
    if response == "3":
        tasks = [{'title': 'HW', 'priority': 'LOW'}, {'title': 'SLEEP', 'priority': 'HIGH'}, {'title': 'EAT', 'priority': 'MEDIUM'}]
        for i in range(0, len(tasks)):
            name_of_task = tasks[i]["title"]
            priority_of_task = tasks[i]["priority"]
            print(f"{i+1} - {name_of_task} - {priority_of_task}")
        input("Press ENTER/RETURN to return to menu: ")
    response = options()

