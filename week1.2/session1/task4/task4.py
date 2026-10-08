# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# "tomato"

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# It displays all items in both fruit and vegtables once.

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("pineapple")
print(fruit)

# Remove an item from vegetables

vegetables.remove("leek")
print(vegetables)

# Find and display symmetric difference of the two sets

print(fruit.symmetric_difference(vegetables))