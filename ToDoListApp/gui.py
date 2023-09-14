import functions
import PySimpleGUI as GUI

label = GUI.Text("Type in a Task")
input_box = GUI.Input(tooltip="Enter Tasks")
add_button = GUI.Button('Add')

window = GUI.Window('My To-Do List App', layout=[[label], [input_box, add_button]])
window.read()
window.close()



