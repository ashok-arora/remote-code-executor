import time, os
from run_docker import DockerRuntime
import subprocess
import platform
import logging

allowed = []

client = None


def setup(volume=os.getcwd()):
    global client
    client = DockerRuntime()
    client.add_volume(v=volume)


def input_expected_output_files(i, e):
    pass

def check_docker_installed():
    cmd = "where" if platform.system() == "Windows" else "which"
    try: 
        subprocess.call([cmd, "docker"])
    except: 
        raise FileNotFoundError


def delete_containers_to_make_space():
    client.cleanup()

def verify_output(output, expected):
    return output == expected or output == expected.strip()


def run(
    file,
    input_file_name=None,
    expected_output=None,
    bool_c=True,
    bool_cpp=True,
    bool_py=True,
    timeout_seconds=10,
):
    global client

    timeout_seconds = int(timeout_seconds)

    try:
        # check file extension, and execute
        if file.lower().endswith(".c") and bool_c:

            output = client.run_c(file, input_file_name, timeout_seconds=timeout_seconds).decode("utf-8")
            # logging.info(repr(output), repr(expected_output), output == expected_output)
            return output == expected_output or output == expected_output.strip()

        elif file.lower().endswith(".py") and bool_py:
            output = client.run_python(file, input_file_name, timeout_seconds=timeout_seconds).decode(
                "utf-8"
            )
            # logging.info(repr(output), repr(expected_output), output == expected_output)
            return output == expected_output or output == expected_output.strip()

        elif file.lower().endswith(".cpp") and bool_cpp:
            output = client.run_cpp(file, input_file_name, timeout_seconds=timeout_seconds).decode(
                "utf-8"
            )
            # logging.info(repr(output), repr(expected_output), output == expected_output)
            return output == expected_output or output == expected_output.strip()

        else:
            logging.info("{} did not execute".format(file))
            return False

    except subprocess.CalledProcessError as e:
        if "FileNotFoundError" in e.output.decode("utf-8"):
            logging.info(
                "{} tried to access a file on the system, malpractice.".format(file)
            )
            return False
        logging.info("{} has syntax error(s)".format(file))
        return False

    except subprocess.TimeoutExpired:
        logging.info("{} timed out".format(file))
        return False
