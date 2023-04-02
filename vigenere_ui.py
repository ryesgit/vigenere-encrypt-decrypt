import PySimpleGUI as sg

sg.theme('DarkBlue')

title = 'VIGENÉRE ENCODER & DECODER'
layout = [
    [sg.Text('', size=(20, 1)), sg.Text(title, justification='center', font=('Helvetica', 20)), sg.Text('', size=(20, 1))],
    [sg.Text('Enter text to encode or decode'), sg.Input(border_width=5, key='input')],
    [sg.T(' ', size=(1,1))],
    [sg.Text('Key: '), sg.Input(pad=(10, 0), border_width=5, key='key')],
    [sg.Text(key='decode-or-encode'), sg.Text(key='value')],
    [sg.Button('Decrypt'), sg.Button('Encrypt')],
    [sg.Button('Quit')]
]

window = sg.Window(title, layout, element_justification='center')

while True:
    event, values = window.read()

    if event == 'Quit' or event == sg.WIN_CLOSED:
        break

window.close()