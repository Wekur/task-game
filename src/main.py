tasks = ("a","b"); 

def listTasks():
    global tasks
    for i in range(len(tasks)):
        print(tasks[i])



tasks += "hellO", 
tasks += "1234", 
listTasks()