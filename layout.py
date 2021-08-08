import PySimpleGUI as sg


def assign_layout():
    tabs = [
        [
            sg.Tab(
                "Files",
                [
                    [
                        # sg.Input("Path to file/folder", size=(80, 1), key='-INPUT-', readonly=True),
                        sg.Input(key="-FILE-", enable_events=True, visible=False),
                        sg.FilesBrowse("File(s)", enable_events=True, target="-FILE-"),
                        sg.Input(key="-FOLDER-", enable_events=True, visible=False),
                        sg.FolderBrowse(
                            "Folder", enable_events=True, target="-FOLDER-"
                        ),
                    ],
                    [
                        sg.Listbox(
                            [], size=(80, 20), right_click_menu=[[]], key="-LIST-"
                        )
                    ],
                    [sg.Button("RUN", key="-RUN-")],
                ],
                element_justification="c",
                key="-FILES-TAB-",
            ),
            sg.Tab(
                "Input",
                [
                    [
                        sg.Input(key="-FILE-INP-", enable_events=True, visible=False),
                        sg.FileBrowse(
                            "Paste from file instead",
                            enable_events=True,
                            target="-FILE-INP-",
                        ),
                    ],
                    [sg.Multiline(size=(800, 600), key="-INP-")],
                ],
            ),
            sg.Tab(
                "Expected Output",
                [
                    [
                        sg.Input(key="-FILE-EXP-", enable_events=True, visible=False),
                        sg.FileBrowse(
                            "Paste from file instead",
                            enable_events=True,
                            target="-FILE-EXP-",
                        ),
                    ],
                    [sg.Multiline(size=(800, 600), key="-EXP-")],
                ],
            ),
            sg.Tab(
                "Results",
                [
                    [sg.Text(" ")],
                    [
                        sg.Table(
                            values=[
                                ["                           ", "       "],
                                ["                           ", "       "],
                            ],
                            headings=["File name", "Result"],
                            display_row_numbers=True,
                            justification="right",
                            col_widths=60,
                            num_rows=10,
                            row_height=35,
                            alternating_row_color="lightyellow",
                            selected_row_colors=("red", "yellow"),
                            key="-RESULT-",
                        )
                    ],
                    [sg.Button("Save to CSV", key="-SAVE-")],
                ],
                element_justification="c",
                key="-RESULT_TAB-",
            ),
            sg.Tab(
                "Settings",
                [
                    [sg.Text(" ")],
                    # [sg.Text(" ")],
                    # [sg.Text(" ")],
                    # [sg.Text(" ")],
                    # [sg.Text(" ")],
                    # [sg.Text(" ")],
                    [sg.Text("Acceptable Languages: ")],
                    [
                        sg.Checkbox("C", default=True, key="-CHECK-C-"),
                        sg.Checkbox("C++", default=True, key="-CHECK-CPP-"),
                        sg.Checkbox("Python", default=True, key="-CHECK-PY-"),
                    ],
                    [
                        sg.Text("Maximum Runtime (in seconds): "),
                        sg.Input("10", key="-TIMEOUT-", size=(6, 1), justification="c"),
                    ],
                ],
            ),
        ]
    ]

    # TODO: Replace with screen dimensions for better support
    tab_group = [
        [sg.TabGroup(tabs, size=(1920, 1080), enable_events=True, key="-TAB_GROUP-")]
    ]

    layout = [[tab_group]]

    window = sg.Window(
        "Remote Code Executor",
        layout,
        size=(800, 600),
        element_justification="c",
        resizable=True,
        finalize=True,
    )

    window["-TIMEOUT-"].Widget.configure(highlightcolor="green", highlightthickness=2)
    window["-EXP-"].Widget.configure(highlightcolor="green", highlightthickness=2)
    window["-INP-"].Widget.configure(highlightcolor="green", highlightthickness=2)
    window["-LIST-"].Widget.configure(highlightcolor="green", highlightthickness=2)

    # window['-INPUT-'].Widget.configure(highlightcolor='grey', highlightthickness=2)

    return window
