import string
import random
import sys

sys.stdout = open("problem_statement_input", "w")

number_of_testcases = 1000
case_set = string.ascii_letters + string.digits + string.punctuation

print(number_of_testcases)
for i in range(number_of_testcases):
    size = random.randint(1, 10)
    testcase = "".join(random.choices(case_set, k=size))
    print(testcase)
