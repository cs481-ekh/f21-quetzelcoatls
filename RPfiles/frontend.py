#!/usr/bin/env python3
import PySimpleGUI as sg
import importlib
UF = importlib.import_module("Unipolar-FWD-DF")
UR = importlib.import_module("Unipolar-REV-DF")
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Steps forward'), sg.InputText(), sg.Button('Fwd')],
            [sg.Text('Steps reverse'), sg.InputText(), sg.Button('Rev')],
            [sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    try:
        if event == "Fwd":
            steps = int(values[0])
            print(f"Forward {steps} steps")
            UF.do_steps_fwd(steps)#call Unipolar code
        elif event == "Rev":
            steps = int(values[1])
            print(f"Reverse {steps} steps")
            UR.do_steps_rev(steps)#call unipolar code
    except ValueError:
        print("Invalid step count specified")

window.close()
