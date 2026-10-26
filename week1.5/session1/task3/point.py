# Week 1.5, Session 1: Task 3
import math


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


# Finally, add code here to demonstrate use of Point
p = Point(1.3,7.2)
print(p.distance())