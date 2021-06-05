from tkinter import Scrollbar

import PySimpleGUI as sg
# from PySimpleGUI.PySimpleGUI import Input

import os
import time

def assign_layout():
    tabs = [
        [
            sg.Tab("Files", [
                [
                    # sg.Input("Path to file/folder", size=(80, 1), key='-INPUT-', readonly=True), 
                    sg.Input(key='-FILE-', enable_events=True, visible=False), sg.FilesBrowse("File(s)", enable_events=True, target='-FILE-'),
                    sg.Input(key='-FOLDER-', enable_events=True, visible=False), sg.FolderBrowse("Folder", enable_events=True, target='-FOLDER-')

                ],
                [
                    # TODO: List of files selected or files inside folder
                    sg.Listbox([], size=(80, 25), right_click_menu=[[]], key='-LIST-')
                    # sg.Multiline("", key='-List-'),

                    # TODO: Button for each entry to RUN the file (attach to the container)
                    # sg.Button("")

                    # for each_file in list_of_files
                ],
                [
                    # TODO: RUN AND CSV buttons
                    sg.Button("RUN", key='-RUN-')
                ]

            ], element_justification='c'),
            sg.Tab("Input", [
                [
                    sg.Multiline(size=(800, 600))
                ]
            ]),
            sg.Tab("Expected Output", [
                [
                    sg.Multiline(size=(800, 600))

                ]
            ]),
            sg.Tab("Results", [
                [
                    sg.Text(" ")
                ],
                [
                    sg.Listbox([], size=(80, 25), right_click_menu=[[]], key='-RESULT-')
                ],
                [
                    sg.Button("Save to CSV", key='-SAVE-')
                ]
            ], element_justification='c')
        ]
    ]

    # TODO: Replace with screen dimensions for better support
    tab_group = [[sg.TabGroup(tabs, size=(1920, 1080))]]
    layout = [[tab_group]]
    window = sg.Window(
        "Remote Code Executor", layout, size=(800, 600), element_justification="c", resizable=True, finalize=True
    )
    # window['-INPUT-'].Widget.configure(highlightcolor='red', highlightthickness=2)
    # window['-INPUT-'].Widget.configure(highlightcolor='grey', highlightthickness=2)

    return window


def main():
    # TODO: Fix color scheme
    sg.theme("Default1")
    # sg.LOOK_AND_FEEL_TABLE["Reddit"] = {
    #     "BACKGROUND": "#ffffff",
    #     "TEXT": "#1a1a1b",
    #     "INPUT": "#dae0e6",
    #     "TEXT_INPUT": "#222222",
    #     "SCROLL": "#a5a4a4",
    #     "BUTTON": ("#FFFFFF", "#0079d3"),
    #     "PROGRESS": ("#0079d3", "#dae0e6"),
    #     "BORDER": 1,
    #     "SLIDER_DEPTH": 0,
    #     "PROGRESS_DEPTH": 0,
    #     "ACCENT1": "#ff5414",
    #     "ACCENT2": "#33a8ff",
    #     "ACCENT3": "#dbf0ff",
    # }

    sg.set_options(font=("Montserrat", 10))
    window = assign_layout()

    l = []

    while True:
        event, values = window.read()
        # print(event, values)
        if event in (None, sg.WINDOW_CLOSED):
            break

        if event in '-FILE-':
            l = list(map(os.path.basename, values['-FILE-'].split(';')))
            window['-LIST-'].update(l)
            window.refresh()

        if event in '-FOLDER-':
            l = os.listdir(values['-FOLDER-'])
            window['-LIST-'].update(l)
            window.refresh()
        
        if event in '-RUN-':
            length = len(l)
            if length == 0:
                sg.popup("No files selected, aborting run.")
            else:
                layout = [[sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress')]]
                progress_window = sg.Window('Running in progress', layout).Finalize()
                progress_bar = progress_window.FindElement('progress')

                for i in range(0, length+1):
                    progress_bar.UpdateBar(i, length)
                    time.sleep(.5)
                time.sleep(.3)
                progress_window.close()
                sg.popup("Run completed, check 'Results' tab")
                # window.finalize()
                # window['-RESULT-'].update(visible=True)
                # window.refresh()


if __name__ == "__main__":
    main()
