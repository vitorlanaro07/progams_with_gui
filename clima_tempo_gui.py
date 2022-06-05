from tkinter import CENTER, font
from numpy import size
import requests
import json
import PySimpleGUI as sg
from unittest import result
import requests
import json
import os

# token: 2e302e06 
# https://api.hgbrasil.com/weather?key=5d9f6f9e&city_name=Japurá,PR (Cidade e Estado)
#


def get_state():
    state = ['RR', 'AP', 'AM', 'PA', 'AC', 'RO', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'MT', 'DF', 'GO', 'MS', 'MG', 'ES', 'RJ', 'SP', 'PR', 'SC', 'RS']
    return(state)


def get_climate(city_name, state_abbr):
    url = f"https://api.hgbrasil.com/weather?key=2e302e06&city_name={city_name},{state_abbr}"
    var_request = requests.get(url).text
    var_request = json.loads(var_request)

    result = var_request['results']
    return(result)


def search_city():
    layout = [[sg.Text(text="Cidade"), sg.Input(key='city_search'), sg.Combo(get_state(), key='state',size=4)],
              [sg.Button("Buscar"), sg.Button("Sair")]]
    return sg.Window("Clima Tempo", layout, finalize=True)


def get_condition(description):
    if description == 'Tempo limpo':
        return r'C:\Users\vitor\Desktop\Aprendendo_Phyton\Meu repo\programs\script_and_gui\img\sunny.png'
    if description == 'Tempo nublado':
        return r'C:\Users\vitor\Desktop\Aprendendo_Phyton\Meu repo\programs\script_and_gui\img\cloudy.png'
    if description == 'Chuva':
        return r'C:\Users\vitor\Desktop\Aprendendo_Phyton\Meu repo\programs\script_and_gui\img\rany.png'
    if description == 'Chuvas esparsas':
        return r'C:\Users\vitor\Desktop\Aprendendo_Phyton\Meu repo\programs\script_and_gui\img\rany.png'
    if description == 'Parcialmente nublado':
        return r'C:\Users\vitor\Desktop\Aprendendo_Phyton\Meu repo\programs\script_and_gui\img\sunny_cloud.png'


def climate(weather, forecast):
    city = weather['city_name']
    clima = weather['temp']
    today = forecast[0]
    tomorrow = forecast[1]
    after_tomorrow = forecast[2]
    after = forecast[3]
    after_after = forecast[4]
    

    layout = [[(sg.Text(text=f'{city}  {clima}°C', font=50,))],
              [sg.Text(today['weekday'], font=30, pad=(35, 0)), sg.Text(tomorrow['weekday'], font=20, pad=(35, 0)), sg.Text(after_tomorrow['weekday'],font=20, pad=(33, 0)), sg.Text(after['weekday'], font=20, pad=(37, 0)), sg.Text(after_after['weekday'], font=20, pad=(33, 0))],
              [sg.Image(get_condition(today['description']), size=(50, 50), pad=(30, 5)), sg.Image(get_condition(tomorrow['description']), size=(50, 50), pad=(30, 0)), sg.Image(get_condition(after_tomorrow['description']), size=(50, 50), pad=(25, 0)), sg.Image(get_condition(after['description']), size=(50, 50), pad=(30, 0)), sg.Image(get_condition(after_after['description']), size=(50, 50), pad=(27, 0))],
              [sg.Text(today['min'], font=16, pad=(38, 5)), sg.Text(tomorrow['min'], font=16, pad=(44, 5)), sg.Text(after_tomorrow['min'], font=16, pad=(38, 5)), sg.Text(after['min'], font=16, pad=(42, 5)), sg.Text(after_after['min'], font=16, pad=(38, 5))],
              [sg.Text(today['max'], font=16, pad=(38, 0)), sg.Text(tomorrow['max'], font=16, pad=(44, 5)), sg.Text(after_tomorrow['max'], font=16, pad=(38, 5)), sg.Text(after['max'], font=16, pad=(42, 5)), sg.Text(after_after['max'], font=16, pad=(38, 5))],
              [sg.Button('Sair',size=25,pad=((170,0)))]
             ]

    return sg.Window("Tempo", layout, finalize=True)


def main():
    window1, window2 = search_city(), None
    city = ''
    state = ''

    while True:
        window, event, values = sg.read_all_windows()
        if (event in (sg.WIN_CLOSED, 'Sair')) and window == window1:
            break

        # Busquei a cidade
        if event == "Buscar" and not window2:
            city = values['city_search']
            state = values['state']
            weather = get_climate(city, state)
            forecast = weather['forecast']
            window1.hide()
            window2 = climate(weather, forecast)

        if window == window2 and (event in (sg.WIN_CLOSED, 'Sair')):
            window2.close()
            window2 = None
            window1.un_hide()


main()
