# Pass the name of the file as argument to program, hardcoded initially. 
# The file's extension is checked and is then executed inside the docker container. 
# Input can also be passed as argument or hardcoded initially. 

# Sample program: Greeter. 
# Input: Name -> str
# Expected Output: Hello ${Name}!

import docker
import time

filename = './test-cases/2019BCS-075.py'
input = 'Ashok'
expected_output = 'Hello Ashok!'

# docker client
client = docker.from_env()

start_time = time.time()

for i in range(1, 81):
    # download base image if not present and run container
    response = client.containers.run('alpine', 'echo hello world ' + str(i) )
    # response = client.containers.run('python:3', 'python' + filename )

    # response is bytestring, print decoded bytestring
    print(response.decode())

# delete all stopped containers
client.containers.prune()

print("--- %.2f seconds ---" % (time.time() - start_time))