import os
import time

import subprocess

import docker


class DockerRuntime:

    client = None
    volumes = None

    def __init__(self) -> None:
        self.client = docker.from_env()

    def add_volume(self, v=os.getcwd()):
        self.volumes = v
        print(v)

    def run_python(self, file, input_file, timeout_seconds):
        output = subprocess.check_output(
            'docker run -v "{}":/tmp:Z python:3-alpine /bin/sh -c "python /tmp/{} < /tmp/{}"'.format(
                self.volumes, file, input_file
            ),
            stderr=subprocess.STDOUT,
            shell=True,
            timeout=timeout_seconds,
        )
        return output

    def run_c(self, file, input_file, timeout_seconds):
        output = subprocess.check_output(
            'docker run -v "{}":/tmp:Z frolvlad/alpine-gcc /bin/sh -c "gcc --static /tmp/{} -o /tmp/qq ; ./tmp/qq < ./tmp/{}; rm /tmp/qq"'.format(
                self.volumes, file, input_file
            ),
            stderr=subprocess.STDOUT,
            shell=True,
            timeout=timeout_seconds,
        )
        return output

    def run_cpp(self, file, input_file, timeout_seconds):
        output = subprocess.check_output(
            'docker run -v "{}":/tmp:Z frolvlad/alpine-gxx /bin/sh -c "c++ --static /tmp/{} -o /tmp/qq ; ./tmp/qq < ./tmp/{} ; rm /tmp/qq"'.format(
                self.volumes, file, input_file
            ),
            stderr=subprocess.STDOUT,
            shell=True,
            timeout=timeout_seconds,
        )
        return output

    def cleanup(self):
        # delete all stopped containers
        self.client.containers.prune()
