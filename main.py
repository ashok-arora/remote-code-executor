from tkinter import Scrollbar
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input


def assign_layout():
    tabs = [
        [
            sg.Tab("Files", [
                [
                    # TODO: Path to file/folder
                    sg.Input("Path to file/folder", size=(80, 1), key='-INPUT-', readonly=True), sg.FilesBrowse("File(s)"), sg.FolderBrowse("Folder")

                ],
                [
                    # TODO: List of files selected or files inside folder
                    sg.Text(""),

                    # TODO: Button for each entry to RUN the file (attach to the container)
                    sg.Button("")

                    # for each_file in list_of_files
                ],
                [
                    # TODO: RUN AND CSV buttons
                    sg.Button("RUN"), sg.Button("Save to CSV")
                ]

            ]),
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
        ]
    ]

    # TODO: Replace with screen dimensions for better support
    tab_group = [[sg.TabGroup(tabs, size=(1920, 1080))]]
    layout = [[tab_group]]
    window = sg.Window(
        "Remote Code Executor", layout, size=(800, 600), element_justification="c", resizable=True, finalize=True
    )
    # window['-INPUT-'].Widget.configure(highlightcolor='red', highlightthickness=2)
    window['-INPUT-'].Widget.configure(highlightcolor='grey', highlightthickness=2)

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
    while True:
        event, values = window.read()
        if event in (None, sg.WINDOW_CLOSED):
            break


if __name__ == "__main__":
    main()
