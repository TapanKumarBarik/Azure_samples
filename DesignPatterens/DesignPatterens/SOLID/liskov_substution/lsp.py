"""
The Liskov Substitution Principle (LSP) is one of the SOLID principles of object-oriented design.
It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
 In other words, if class B is a subclass of class A, then objects of type A should be replaceable with objects of type B without altering the desirable properties of the program.
"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def set_width(self, width: int):
        self._width = width

    def set_height(self, height: int):
        self._height = height

    def get_area(self):
        return self._width * self._height


class Square(Rectangle):
    def set_width(self, width: int):
        self._width = width
        self._height = width  # Square maintains equal width and height

    def set_height(self, height: int):
        self._height = height
        self._width = height  # Square maintains equal width and height

# Function to test the area calculation
def print_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    print(f"Expected area: 50, Got: {rectangle.get_area()}")

# Test with Rectangle
rect = Rectangle(2, 3)
print_area(rect)  # Expected area: 50, Got: 50

# Test with Square (This will violate LSP)
sq = Square(2, 2)
print_area(sq)  # Expected area: 50, Got: 100
