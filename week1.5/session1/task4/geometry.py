# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, xCord, yCord):
        self.x = xCord
        self.y = yCord

    # Add distance() method here
    def distance(self):
        return math.hypot(self.x,self.y)


    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distanceTo(self,otherX, otherY):
        return math.hypot(self.x,self.y,otherX,otherY)


# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

class Circle:
    def __init__(self,centre,radius):
        self.point = centre
        self.radius = radius

    def area(self,radius):
        return round(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938 * radius * radius, 5)

    def perimeter(self,radius):
        return round(radius * 2 * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938,5)