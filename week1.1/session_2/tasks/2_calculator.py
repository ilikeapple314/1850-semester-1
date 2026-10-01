# Fill out the code to make a very simple calculator

# ask the user to enter number1:
num1 = input("Enter a number: ")

# ask the user to enter number 2:
num2 = input("Enter a 2nd number: ")

operation = input("What operation do you want to complete (+,-,x,/): ")

while (operation != "+") and (operation != "-") and (operation != "x") and (operation != "/"):
    operation = input("Please enter an operation (+,-,x,/): ")


 # calculate the result of adding those numbers together
if(operation == "+"):
    solution = int(num1) + int(num2)
elif(operation == "-"):
    solution = int(num1) - int(num2)
elif(operation == "x"):
    solution = int(num1) * int(num2)
else:
    solution = int(num1) / int(num2)




# print out the answer
print(solution)
