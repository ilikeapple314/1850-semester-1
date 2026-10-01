# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")

# make all characters lowercase
print(f"Modified String 1: {user_string.lower()}")

# make all characters uppercase
print(f"Modified String 2: {user_string.upper()}")

# apparently this returns a trimmed version of the string
print(f"Modified String 3: {user_string.strip()}")

# replaces all a's with @
print(f"Modified String 4: {user_string.replace('a', '@')}")

#  capitalizes the first letter and the rest become lowercase
print(f"Modified String 5: {user_string.capitalize()}")

# flips the string
print(f"Modified String 6: {user_string[::-1]}")

# capitalizes each word 
print(f"Modified String 7: {user_string.title()}")

# returns the number of characters in the string
print(f"Modified String 8: {len(user_string)}")

# searches for a character if it found returns its place in the string
print(f"Modified String 9: {user_string.find('a')}")

# finds the number of given characters in the string
print(f"Modified String 10: {user_string.count('a')}")

# it checks if a string starts with a given string
print(f"Modified String 11: {user_string.startswith('Hello')}")

# it checks if a string ends with a given string
print(f"Modified String 12: {user_string.endswith('!')}")

# returns true if all characters are alphanumeric
print(f"Modified String 13: {user_string.isalnum()}")

# returns true if all the characters are in the alphabet
print(f"Modified String 14: {user_string.isalpha()}")

# returns true if all characters are digits
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!