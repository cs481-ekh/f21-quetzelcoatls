#!/usr/bin/env python3
import PySimpleGUI as sg
import importlib
UF = importlib.import_module("Unipolar-FWD-DF")
UR = importlib.import_module("Unipolar-REV-DF")
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Steps forward'), sg.InputText(), sg.Button('Fwd')],
            [sg.Text('Steps reverse'), sg.InputText(), sg.Button('Rev')],
            [sg.Button('Return to 0')],
            [sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
forwardCount = 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    try:
        if event == "Fwd":
            steps = int(values[0])
            print(f"Forward {steps} steps")
            forwardCount+=steps
            UF.do_steps_fwd(steps)#call Unipolar code
        elif event == "Rev":
            steps = int(values[1])
            print(f"Reverse {steps} steps")
            if (forwardCount-steps < 0):
                forwardCount = 0
            else:
                forwardCount-=steps
            UR.do_steps_rev(steps)#call unipolar code
        elif event == "Return to 0":
            if forwardCount > 0:
                print(f"Reverse {forwardCount} steps")
                UR.do_steps_rev(steps)#call unipolar code
                forwardCount = 0
            elif forwardCount < 0:
                print(f"Error! Negative Steps!")
            else:
                print("Stepper is already at 0")
    except ValueError:
        print("Invalid step count specified")

window.close()
