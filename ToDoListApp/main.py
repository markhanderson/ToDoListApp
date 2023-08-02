# from functions import get_tasks, write_tasksimport functions
# from modules import functions
import functions

while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("Add"):
        task = user_action[4:]

        tasks = functions.get_tasks()

        tasks.append(task + '\n')

        functions.write_tasks(tasks)

    elif user_action.startswith('Show'):

        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            tasks = functions.get_tasks()

            new_task = input("Enter New Task: ")
            tasks[number] = new_task + '\n'

            functions.write_tasks(tasks)

        except ValueError:
            print("Your Command is Not Valid, Please try again.")
            continue

    elif user_action.startswith('Complete'):
        try:
            number = int(user_action[9:])

            tasks = functions.get_tasks()

            index = number - 1
            tasks_to_remove = tasks[index].strip('\n')
            tasks.pop(number - 1)

            functions.write_tasks(tasks)

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
