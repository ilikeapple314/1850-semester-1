# Worksheet 1.2: Task 1 Solution
import sys


grade = input("Enter grade between 0-100: ")

if(grade.isdigit()):
    grade = int(grade)
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")



if not(0 <= grade <= 100):
    sys.exit("Error: Grade must be an integer between 0 and 100")

if(100 >= grade >= 70):
    print(f"{grade} is a Distinction")
elif(40 <= grade <= 69):
    print(f"{grade} is a Pass")
elif(0 <= grade <= 39):
    print(f"{grade} is a Fail")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")