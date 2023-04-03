'''
NAME: Abubakar Sadiq Yusuf
ID: 10968467
DEPARMENT: Biomedical Engineering

'''

import qrcode as qr
import PySimpleGUI as sg 

sg.theme('DarkPurple7')
font =('Verdana', 13)

qr_image = [sg.Image('', key = 'qr_code')]


index = 0
color = {0: ("white", "blue"), 1: ("red", "green")}
layout = [
    [sg.Text('Enter URL:'), sg.Input(text_color= 'black', key= 'URL' )],
    [sg.Button('Create', key='Submit',  mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE', size= (7,1))],
    [sg.Column([qr_image], justification= 'center')],
]

 
window = sg.Window('QR Code Generator', layout, font= font)


while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'Submit':
        url = values['URL']
        if url:
            image = qr.make(url)
            image.save('qr.png')
            window['qr_code'].update('qr.png')

window.close()