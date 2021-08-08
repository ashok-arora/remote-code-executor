import sys
import re

sys.stdout = open("problem_statement_output", "w")

f = open("problem_statement_input", "r")

number_of_testcases = f.readline()

for x in f:
    regex = re.compile("[^a-zA-Z]")
    if regex.sub("", x) == "":
        print("-1")
    else:
        print(regex.sub("", x))
