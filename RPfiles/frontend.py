#!/usr/bin/env python3

import test.mock_window as sg
# import PySimpleGUI as sg

forward_script = "mock/Mock-FWD-DF.py"
reverse_script = "mock/Mock-REV-DF.py"

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button("Stop", key="Stop", visible=False), sg.Text("", key="Status")],
            [sg.Text('Steps forward'), sg.InputText(), sg.Button('Fwd', key="Fwd")],
            [sg.Text('Steps reverse'), sg.InputText(), sg.Button('Rev', key="Rev")],
            [sg.Button('Return to 0', key="Ret0")],
            [sg.Button('Close', key="Close")]
          ]

def set_ui_enabled_state(enabled: bool):
    window["Rev"].Update(disabled=(not enabled))
    window["Fwd"].Update(disabled=(not enabled))
    window["Ret0"].Update(disabled=(not enabled))
    window["Close"].Update(disabled=(not enabled))

    window.Refresh()

def move_steps(window, script: str, steps: int) -> bool:
    window["Status"].Update("Starting...")
    window["Stop"].Update(visible=True)
    set_ui_enabled_state(False)

    steps_taken = 0
    while steps_taken < steps:
        # Check if we want to cancel
        event, values = window.read(timeout=1)
        if event == "Stop":
            break

        iteration_steps = min(5, steps-steps_taken)

        sg.execute_command_subprocess(
            "python3",
            *[script, str(iteration_steps)],
            wait=True
        )

        steps_taken += iteration_steps

        window["Status"].Update(f"Steps: {steps_taken} / {steps} ({script})")
        window.Refresh()


    window["Status"].Update(f"Finished. Moved {steps_taken} steps ({script}).")
    window["Stop"].Update(visible=False)
    set_ui_enabled_state(True)

    return True

# Create the Window
window = sg.Window('Stretcher-Matic 9000', layout)
forwardCount = 0
# Event Loop to process "events" and get the "values" of the inputs

while 1:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks close
        break
    try:
        if event == "Fwd":
            steps = int(values[0])
            print(f"Forward {steps} steps")
            forwardCount+=steps
            move_steps(window, forward_script, steps)
        elif event == "Rev":
            steps = int(values[1])
            print(f"Reverse {steps} steps")
            if (forwardCount-steps < 0):
                forwardCount = 0
            else:
                forwardCount-=steps
            move_steps(window, reverse_script, steps)
        elif event == "Return to 0":
            if forwardCount > 0:
                print(f"Reverse {forwardCount} steps")
                move_steps(window, reverse_script, steps)
                forwardCount = 0
            elif forwardCount < 0:
                print(f"Error! Negative Steps!")
            else:
                print("Stepper is already at 0")
    except ValueError:
        print("Invalid step count specified")

window.close()
