
def cel_fah(celsius):
    return (celsius * 9/5) + 32


def fah_cel(fahr):
    return (fahr - 32) * 5/9


layout = [
    [sg.Text('Temperatura:'), sg.InputText(key='entrada')],
    [sg.Button('Celsius'), sg.Button('Fahrenheit')],
]


window = sg.Window('\t\t\t\t\t Conversor de Temperatura', layout)

while True:

    event, values = window.read()


    if event == sg.WIN_CLOSED:
        break


    elif event == 'Celsius':
        try:

            celsius = float(values['entrada'])


            fahrenheit = cel_fah(celsius)


            sg.popup(f'{celsius} Celsius é igual a {fahrenheit} Fahrenheit')
        except ValueError:
            sg.popup('Insira um número válido para Celsius')


    elif event == 'Fahrenheit':
        try:

            fahrenheit = float(values['entrada'])


            celsius = fah_cel(fahrenheit)


            sg.popup(f'{fahrenheit} Fahrenheit é igual a {celsius} Celsius')
        except ValueError:
            sg.popup('Insira um número válido para Fahrenheit')


window.close()