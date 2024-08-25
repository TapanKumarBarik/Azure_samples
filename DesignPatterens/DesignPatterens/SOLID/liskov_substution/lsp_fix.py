class Shape:
    def get_area(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def set_width(self, width: int):
        self._width = width

    def set_height(self, height: int):
        self._height = height

    def get_area(self):
        return self._width * self._height


class Square(Shape):
    def __init__(self, side: int):
        self._side = side

    def set_side(self, side: int):
        self._side = side

    def get_area(self):
        return self._side * self._side

# Function to test the area calculation
def print_area(shape: Shape):
    if isinstance(shape, Rectangle):
        shape.set_width(5)
        shape.set_height(10)
    elif isinstance(shape, Square):
        shape.set_side(5)
    print(f"Area: {shape.get_area()}")

# Test with Rectangle
rect = Rectangle(2, 3)
print_area(rect)  # Area: 50

# Test with Square
sq = Square(2)
print_area(sq)  # Area: 25
