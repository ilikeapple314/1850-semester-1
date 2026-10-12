# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# because fruit eventually runs out of items when this happens the while loops treats it as a false boolean statement

# What features of Python does it rely on?
# in this case it relys on the fact that it is treated as an object and using this the list fruit can also be treated as a boolean variable
