# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

import geometry

cc = geometry.Point(12,28)
c = geometry.Circle(10,cc)
p = geometry.Point(15,20)

if p in c:
    print("The point is within the circle")
else:
    print("The point is not within the circle")