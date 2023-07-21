

def get_tasks(filepath='tasks.txt'):
    """ Read a task and return a list tasks
    from the tasks text file.
    """
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local

def write_tasks(tasks_arg, filepath="tasks.txt"):
    """ Write a task and return a list of tasks
    from the tasks text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)


while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("Add"):
        task = user_action[4:]

        tasks = get_tasks()

        tasks.append(task + '\n')

        write_tasks(tasks)

    elif user_action.startswith('Show'):

        tasks = get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            tasks = get_tasks()

            new_task = input("Enter New Task: ")
            tasks[number] = new_task + '\n'

            write_tasks(tasks)

        except ValueError:
            print("Your Command is Not Valid, Please try again.")
            continue

    elif user_action.startswith('Complete'):
        try:
            number = int(user_action[9:])

            tasks = get_tasks()

            index = number - 1
            tasks_to_remove = tasks[index].strip('\n')
            tasks.pop(number - 1)

            write_tasks(tasks)

            message = f'task {tasks_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print("There is No Task with that Number, please try again. ")
        continue

    elif user_action.startswith('Exit'):
        break

    else:
        print('Command is not valid.')

print("Bye!")
