import PySimpleGUI as sg
vidgeti = [
    [sg.Text('Имя'), sg.InputText(key='Игрок', default_text= 'Xlerian')],
    # [sg.Text("Размер"), sg.OptionMenu(values = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], default_value = 25, key= 'Размер')],
    [sg.Button('Выход'), sg.Button('Старт')]
]
a = 0
okno = sg.Window('Змейка', vidgeti)
while a == 0:
    sobytie = okno.read()
    if sobytie[0] == 'Выход' or sobytie[0] == 'Старт' or sobytie[0] == None:
        a = 1
    print(sobytie[0])
    sobitiya = sobytie[1]
    sobitiya_knopok = sobytie[0]