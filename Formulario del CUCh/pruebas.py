import PySimpleGUI as sg

layout = [[sg.Text('Enter a filename:')],
          [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse()],
          [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]]

window = sg.Window("Don't Even Try It", layout).Finalize()
window.Maximize()
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Save':
        sg.user_settings_set_entry('-filename-', values['-IN-'])

window.close()