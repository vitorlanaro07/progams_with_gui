from matplotlib.pyplot import pause
import psutil as ps
import time
import PySimpleGUI as sg

# Coletar dados do meu PC
# Converter esses dados em graficos
# Utilizar interface grafica


def get_memory():
    for x in range(10):
        memory = ps.swap_memory()
        return(memory[0])


sg.theme('Dark Blue 3')

layout = [
    [sg.Text(text="Leitor de dados", font=50, justification='center')],
    [sg.Text(f"Memoria usada: {get_memory()}")],
]

window = sg.Window("Coletor de dados", layout,
                   size=(600, 600), auto_size_text=False,)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
