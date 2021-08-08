import csv
import os
import time
from datetime import datetime
import PySimpleGUI as sg
import logging
import backend
import string
import random


from layout import assign_layout

file_name = "rce_log_" + datetime.now().strftime("%Y%m%d-%H%M%S")
logging.basicConfig(
    filename=file_name,
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.CRITICAL,
)


def main():

    sg.theme("Default1")
    sg.set_options(font=("Montserrat", 10))

    window = assign_layout()

    run_completed = False

    l = []

    results = []

    volume_to_mount = None

    while True:
        event, values = window.read()
        # print(event, values)

        if event in (None, sg.WINDOW_CLOSED):
            break

        # select a group of files
        if event == "-FILE-":
            try:
                l = list(map(os.path.basename, values["-FILE-"].split(";")))
                volume_to_mount = os.path.dirname(values["-FILE-"].split(";")[0])

            except FileNotFoundError:
                pass

            window["-LIST-"].update(l)
            window.refresh()

            results = []

        # select a folder (all files inside will be selected)
        if event == "-FOLDER-":
            try:
                l = os.listdir(values["-FOLDER-"])
            except FileNotFoundError:
                pass

            window["-LIST-"].update(l)
            window.refresh()

            volume_to_mount = values["-FOLDER-"]

            results = []

        if event in ("-FILE-INP-", "-FILE-EXP-"):
            try:
                filename = values[event]
                with open(filename, "rt", encoding="utf-8") as f:
                    text = f.read()

                values["-" + event.split("-")[2] + "-"] = text
                window["-" + event.split("-")[2] + "-"].update(text)
                window.refresh()
            except FileNotFoundError:
                pass

        # after selecting the files, run them
        if event == "-RUN-":

            try:
                backend.check_docker_installed()
            except FileNotFoundError:
                sg.popup("Docker not installed! Can't proceed!!")
                continue

            # save input before running
            case_set = string.ascii_letters
            
            input_file = "input_" + "".join(random.choices(case_set, k=5))

            f = open(volume_to_mount + '/' + input_file, "w")
            f.write(values["-INP-"])
            f.close()

            length = len(l)

            if length == 0:
                sg.popup("No files selected, aborting run.")

            else:

                layout = [
                    [sg.ProgressBar(1, orientation="h", size=(20, 20), key="progress")]
                ]

                progress_window = sg.Window("Running in progress", layout).Finalize()
                progress_bar = progress_window.FindElement("progress")

                backend.setup(volume_to_mount)

                # the files are executed here
                for i in range(0, length):

                    if l[i] == input_file:
                        continue

                    result = backend.run(
                        l[i],
                        input_file,
                        values["-EXP-"],
                        values["-CHECK-C-"],
                        values["-CHECK-CPP-"],
                        values["-CHECK-PY-"],
                        values["-TIMEOUT-"],
                    )

                    if result == False:
                        results.append("Fail")
                    else:
                        results.append("Pass")
                    progress_bar.UpdateBar(i, length)

                time.sleep(0.3)
                progress_window.close()
                sg.popup("Run completed, check 'Results' tab")

                run_completed = True
                os.remove(volume_to_mount + '/' + input_file)
                backend.delete_containers_to_make_space()

        if values["-TAB_GROUP-"] == "-RESULT_TAB-":
            if run_completed:
                vals = [list(e) for e in zip(l, results)]
                window["-RESULT-"].update(values=vals)

            else:
                sg.popup("Run first to view results.")
                window.Element("-FILES-TAB-").select()

        if event == "-SAVE-":
            filename = volume_to_mount + "/" + "results_" + datetime.now().strftime("%Y%m%d-%H%M%S")
            vals = [list(e) for e in zip(l, results)]

            with open(filename + ".csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["File name", "Result"])
                writer.writerows(vals)
            sg.popup("File saved as " + filename + ".csv")


    logging.shutdown()
    if os.stat(file_name).st_size == 0: 
        os.remove(file_name)

if __name__ == "__main__":
    main()

# sudo pip3 install -q pipenv

# pipenv install --ignore-pipfile
# pipenv run pyinstaller --onefile --name rce --clean --log-level ERROR main.py


