
while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if 'Add' in user_action:
        task = user_action[4:]

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        tasks.append(task)

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

        # file = open('tasks.txt', 'w')
        # file.writelines(tasks)
        # file.close()

    elif 'Show' in user_action:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()


        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'Edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        new_task = input("Enter New Task: ")
        tasks[number] = new_task + '\n'

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

    elif 'Complete' in user_action:
        number = int(user_action[9:])

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        index = number - 1
        tasks_to_remove = tasks[index].strip('\n')
        tasks.pop(number - 1)

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

        message = f'task {tasks_to_remove} was removed from the list.'
        print(message)

    elif 'Exit' in user_action:
        break

    else:
        print('Command is not valid.')


print("Bye!")












