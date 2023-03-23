
while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'Add':
            task = input("Enter a Task: ") + "\n"

            file = open('tasks.txt', 'r')
            tasks = file.readlines()
            file.close()

            tasks.append(task)

            file = open('tasks.txt', 'w')
            file.writelines(tasks)
            file.close()

        case "Show" | "Display":
            for index, item in enumerate(tasks):
                row = f"{index + 1}-{item}"
                print(row)
        case 'Edit':
            number = int(input("Number of Task to Edit"))
            number = number - 1
            new_task = input("Enter New Task: ")
            tasks[number] = new_task
        case 'Complete':
            number = int(input("Number of Task to Complete"))
            tasks.pop(number - 1)
        case 'Exit':
            print("You Entered a Unknown Command, Please Try Again.")
            break

print("Bye!")












