from cgitb import text
import math
from time import time
from tkinter import Button
from wsgiref.validate import validator
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Input('', size=(21, 10), key='input')],
    [sg.Button('√'), sg.Button('/'), sg.Button('*'), sg.Button('+')],
    [sg.Button(7), sg.Button(8), sg.Button(9), sg.Button('-')],
    [sg.Button(4), sg.Button(5), sg.Button(6), sg.Button('=')],
    [sg.Button(1), sg.Button(2), sg.Button(3), sg.Button('⏎')],
    [sg.Button('CE'), sg.Button(0), sg.Button('.')]
]

window = sg.Window('Calculadora', layout, auto_size_buttons=False,
                   default_button_element_size=(4, 2), font=12)


key_entered = ''
while True:
    event, values = window.read()
    #print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'CE':
        key_entered = ''
    else:
        key_entered = values['input']
        key_entered += event
        # print(key_entered)
    if event == '=':
        key_entered = eval(values['input'])
    elif event == '√':
        key_entered = math.sqrt(float(values['input']))
    elif event == '⏎':
        key_entered = str(values['input'])[:-1]

    print(event, values)
    window['input'].update(key_entered)


window.close()
