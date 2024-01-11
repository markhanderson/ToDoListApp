import functions
import PySimpleGUI as GUI

label = GUI.Text("Type in a Task")
input_box = GUI.Input(tooltip="Enter Tasks", key="task")
add_button = GUI.Button('Add')
list_box = GUI.Listbox(values=functions.get_tasks(), key='tasks',
                       enable_events=True, size=[45, 10])

edit_button = GUI.Button('Edit')
complete_button = GUI.Button("Complete")
exit_button = GUI.Button('Exit')

#layout = [[label],
#         [input_box, add_button],
#        [list_box, edit_button, complete_button],
#       [exit_button]]

window = GUI.Window('My To-Do List App',
                    layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['tasks'])
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case 'Edit':
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
        case "Complete":
            tasks_to_complete = values['tasks'][0]
            tasks = functions.get_tasks()
            tasks.remove(tasks_to_complete)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['tasks'].update(value='')
        case 'Exit':
            break
        case 'tasks':
            window['task'].update(value=values['tasks'][0])
        case GUI.WIN_CLOSED:
            break

window.close()



