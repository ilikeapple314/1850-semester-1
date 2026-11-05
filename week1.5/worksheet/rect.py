# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not isinstance(width,int) or not isinstance(height,int):
            raise TypeError("Width and height must be intergers.")

        if (width<=0) or (height<=0):
            raise ValueError("Width and height must be more than 0.")

        
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
        """
        Boolean function to determine if a rectangle is a square
        """
        if(self.width == self.height):
            return True
        else:
            return False

    def area(self):
        """
        Finds the area of a given rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """
        Finds the perimeter of a given rectangle
        """
        return ((self.height * 2) + (2 * self.width))

