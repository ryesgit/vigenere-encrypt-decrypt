import PySimpleGUI as sg

sg.theme('DarkBlue')

title = 'VIGENÉRE ENCODER & DECODER'
layout = [
    [sg.Text('', size=(20, 1)), sg.Text(title, justification='center', font=('Helvetica', 20)), sg.Text('', size=(20, 1))],
    [sg.Text('Enter text to encode or decode'), sg.InputText(pad=(10, 0), border_width=5)],
    [sg.Text(key='decode-or-encode'), sg.Text(key='value')],
    [sg.Button('Decrypt'), sg.Button('Encrypt')],
    [sg.Button('Quit')]
]

window = sg.Window(title, layout)

while True:
    event, values = window.read()

    if event == 'Quit' or event == sg.WIN_CLOSED:
        break

window.close()