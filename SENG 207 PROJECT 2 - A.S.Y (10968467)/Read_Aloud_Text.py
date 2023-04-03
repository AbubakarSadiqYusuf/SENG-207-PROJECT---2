'''
NAME: Abubakar Sadiq Yusuf
ID: 10968467
DEPARTMENT: Biomedical Engineering

'''
# CREATING A TEXT TO SPEECH APP THAT READS OUT ANY GIVEN TEXT.
import PySimpleGUI as sg
import pyttsx3
sg.theme('Topanga')
read_aloud_text_engine = pyttsx3.init()
vocal_variety = read_aloud_text_engine.getProperty('voices')

color = {0: ("white", "blue"), 1: ("yellow", "green")}
layout = [  [sg.Text('Enter text:', text_color = 'white', background_color = 'purple')],
            [sg.InputText(key = 'user_input'),sg.Button('Read Entered Text',button_color = 'grey')] ,
            [sg.Text('Select Speaker:',text_color = 'gold', background_color = 'grey'),sg.Radio('Male', 'RADIO1', default=True, key = 'male',text_color= 'white', background_color = 'red'),sg.Radio('Female', 'RADIO1', key = 'female',text_color ='black', background_color = 'pink' )],
]

window = sg.Window('Read Aloud Text App', layout,background_color = 'grey')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Read Entered Text':
        text = values['user_input']
        if values['male']:
            read_aloud_text_engine.setProperty('voice', vocal_variety[0].id )
        elif values['female']:
            read_aloud_text_engine.setProperty('voice', vocal_variety[1].id)


        read_aloud_text_engine.say(text)
        read_aloud_text_engine.runAndWait()


window.close()
