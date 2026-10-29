# Week 1.5, Session 2: Task 1

# Add type checking to the constructor of Point

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            self.x = x
            self.y = y
        else:
            raise TypeError("x and y must be numbers")



    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Test program

p = Point("two", "one")
print(p.distance())
