# Worksheet 1.2: Task 2 Solution
import sys
import math
from util import read_numbers

try:
    numbers = read_numbers()
except:
    sys.exit("Error: no numbers provided")

print(numbers)

maximum = numbers[0]
minimum = numbers[0]
mean = 0
median = 0
totalNumbers = 0
totalOfNumbers = 0

for number in numbers:
    if (number > maximum):
        maximum = number
    elif(number < minimum):
        minimum = number

    totalNumbers = totalNumbers + 1
    totalOfNumbers = totalOfNumbers + number

mean = totalOfNumbers / totalNumbers

numbers.sort()
print(totalNumbers)

if (totalNumbers % 2 == 0):
    middle = math.trunc(totalNumbers / 2)
    median = (numbers[middle - 1] + numbers[middle]) / 2


else:
    median = numbers[math.trunc(totalNumbers / 2)]


print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
