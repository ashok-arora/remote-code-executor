import PySimpleGUI as sg


def assign_layout():
    layout = [[]]
    window = sg.Window(
        "Remote Code Executor", layout, size=(800, 600), element_justification="c"
    )
    return window


def main():
    sg.theme("Reddit")
    sg.set_options(font=("Montserrat", 10))
    window = assign_layout()
    while True:
        event, values = window.read()
        if event in (None,sg.WINDOW_CLOSED):
            break


if __name__ == "__main__":
    main()