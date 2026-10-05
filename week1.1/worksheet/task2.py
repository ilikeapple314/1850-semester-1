"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Aaron Rich 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
monthlySaving = input("How much money do you want to save each month?: ")

# Validate that they have entered an integer.

#####################################################################
#    My better solution :)
#    while(monthlySaving.isdigit() == False):
#    monthlySaving = input("Please enter a number:")
#####################################################################

if(monthlySaving.isdigit() == False):
    print("Invalid Amount")
    exit()



monthlySaving = int(monthlySaving)

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
yearlySaving = monthlySaving * 12

# print this out for the user with a suitable message.
print(f"{name} you will save £{yearlySaving} this year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.

# I had to look up how to force trailing zeros (source:https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros) I assume this is fine but I thought I should make this expicit given the decliration at the start of the code and the importance placed on Academic intgrity. Please comfirm if this is acceptable in future portfollio tasks #
totalAmount = '{:.2f}'.format(round(yearlySaving * 1.008),2)

# print this out in the format £X.XX (to two decimal places).
print(f"Total: £{totalAmount}")

