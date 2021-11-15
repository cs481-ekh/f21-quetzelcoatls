#!/usr/bin/env python3
import PySimpleGUI as sg
import re

forward_script = "mock/Mock-FWD-DF.py"
reverse_script = "mock/Mock-REV-DF.py"

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button("Stop", key="Stop", visible=False), sg.Text(key="Status")],
            [sg.Text('Micrometer input'), sg.InputText(key="micro",enable_events = True, do_not_clear=True)],
            [sg.ProgressBar(max_value=0, key="ProgressBar", visible=False)],
            [sg.Text('Steps forward'), sg.InputText(), sg.Button('Fwd', key="Fwd")],
            [sg.Text('Steps reverse'), sg.InputText(), sg.Button('Rev', key="Rev")],
            [sg.Text('Steps taken: '), sg.Text(size=(15,1), key='OUTPUT')],
            [sg.Button('Return to 0', key="Ret0")],
            [sg.Button('Close', key="Close")]
          ]

def set_ui_enabled_state(enabled: bool):
    window["Rev"].Update(disabled=(not enabled))
    window["Fwd"].Update(disabled=(not enabled))
    window["Ret0"].Update(disabled=(not enabled))
    window["Close"].Update(disabled=(not enabled))

    window.Refresh()

def move_steps(window, script: str, steps: int) -> int:
    window["Status"].Update("Starting...")
    window["Stop"].Update(visible=True)
    window["ProgressBar"].Update(0, max=steps, visible=True)
    set_ui_enabled_state(False)

    steps_taken = 0
    while steps_taken < steps:
        # Check if we want to cancel
        event, values = window.read(timeout=1)
        if event == "Stop":
            break
        iteration_steps = min(5, steps-steps_taken)

        sp = sg.execute_command_subprocess(
            "python3",
            *[script, str(iteration_steps)],
            wait=True
        )
        if sp.returncode != 0:
            sg.popup_error(f'Exception {sp.returncode}!')
            break
        steps_taken += iteration_steps
        
        window["Status"].Update(f"Steps: {steps_taken} / {steps} ({script})")
        window["ProgressBar"].Update(steps_taken, max=steps, visible=True)
        window.Refresh()


    window["Status"].Update(f"Finished. Moved {steps_taken} steps ({script}).")
    window["Stop"].Update(visible=False)
    window["ProgressBar"].Update(0, max=steps, visible=False)
    set_ui_enabled_state(True)

    return steps_taken

# Create the Window
window = sg.Window('Stretcher-Matic 9000', layout)
stepsTracker = 0
# Event Loop to process "events" and get the "values" of the inputs

while 1:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks close
        break
    try:
        if event == "Fwd":
            steps = int(values[0])
            print(f"Forward {steps} steps")
            stepsTracker += move_steps(window, forward_script, steps)
        elif event == "Rev":
            steps = int(values[1])
            print(f"Reverse {steps} steps")
            stepsTracker -= move_steps(window, reverse_script, steps)
        elif event == "Ret0":
            if stepsTracker > 0:
                print(f"Reverse {stepsTracker} steps")
                stepsTracker -= move_steps(window, reverse_script, stepsTracker)
            elif stepsTracker < 0:
                print(f"Forward {stepsTracker*-1} steps")
                stepsTracker += move_steps(window, forward_script, -stepsTracker)
            else:
                print("Stepper is already at 0")
        elif event == "micro":
            if not re.fullmatch("\d(\.(\d(\d{1,2})?)?)?",values["micro"]):
                old = re.match("\d\.\d{2,3}\s+",values["micro"]) #button has been pressed multiple times
                if old:
                    window["micro"].update(values["micro"][old.end():])
                else:
                    window["micro"].update("")
            if len(values["micro"]) == 4:
              print(f"True Displacement: {values['micro']}", end='', flush=True)
            elif len(values["micro"]) == 5:
              print(f"{values['micro'][4]}")

    except ValueError:
        print("Invalid step count specified")
    window['OUTPUT'].update(stepsTracker)

window.close()
