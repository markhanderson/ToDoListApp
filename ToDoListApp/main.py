
while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'Add':
            task = input("Enter a Task: ") + "\n"

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()

            tasks.append(task)

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

            file = open('tasks.txt', 'w')
            file.writelines(tasks)
            file.close()

        case 'Show':

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()


            for index, item in enumerate(tasks):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'Edit':
            number = int(input("Number of Task to Edit"))
            number = number - 1

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
            print('Here are the existing tasks', tasks)



            new_task = input("Enter New Task: ")
            tasks[number] = new_task + '\n'

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

        case 'Complete':
            number = int(input("Number of Task to Complete"))

            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
            index = number - 1
            tasks_to_remove = tasks[index].strip('\n')
            tasks.pop(number - 1)

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

            message = f'task {tasks_to_remove} was removed from the list.'
            print(message)

        case 'Exit':
            print("You Entered a Unknown Command, Please Try Again.")
            break

print("Bye!")












