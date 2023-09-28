import functions
import PySimpleGUI as GUI

label = GUI.Text("Type in a Task")
input_box = GUI.Input(tooltip="Enter Tasks", key="task")
add_button = GUI.Button('Add')

window = GUI.Window('My To-Do List App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case GUI.WIN_CLOSED:
            break

window.close()



