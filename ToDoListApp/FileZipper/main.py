import PySimpleGUI as GUI

label1 = GUI.Text("Select files to compress")
input1 = GUI.Input()
choose_button1 = GUI.FilesBrowse("Choose")

label2 = GUI.Text("Select destination folder")
input2 = GUI.Input()
choose_button2 = GUI.FolderBrowse("Choose")
compress_button = GUI.Button('Compress')

window = GUI.Window("File Compressor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button]])

window.read()
window.close()

