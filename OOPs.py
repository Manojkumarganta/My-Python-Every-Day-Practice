from abc import ABC, abstractmethod

# ------------------- ABSTRACTION -------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# ------------------- ENCAPSULATION + INHERITANCE -------------------
class Rectangle(Shape):
    shape_type = "2D Shape"  # Class variable (shared by all objects)

    def __init__(self, length, width):
        self.__length = length      # private variable
        self._width = width         # protected variable

    # getter and setter for private variable
    def get_length(self):
        return self.__length

    def set_length(self, new_length):
        if new_length > 0:
            self.__length = new_length
        else:
            print("Length must be positive!")

    # implementation of abstract methods
    def area(self):
        return self.__length * self._width

    def perimeter(self):
        return 2 * (self.__length + self._width)

    # class method
    @classmethod
    def description(cls):
        return f"This is a {cls.shape_type}."

    # static method
    @staticmethod
    def is_shape():
        return True


# ------------------- INHERITANCE + POLYMORPHISM -------------------
class Square(Rectangle):
    def __init__(self, side):
        # calling parent constructor
        super().__init__(side, side)

    # overriding method
    def perimeter(self):
        return 4 * self.get_length()


# ------------------- MULTIPLE INHERITANCE -------------------
class Color:
    def __init__(self, color):
        self.color = color

    def show_color(self):
        return f"Color: {self.color}"


class ColoredSquare(Square, Color):
    def __init__(self, side, color):
        Square.__init__(self, side)
        Color.__init__(self, color)

    # method overloading (achieved using default arguments)
    def display(self, show_area=True):
        if show_area:
            return f"{self.show_color()} | Area: {self.area()}"
        else:
            return self.show_color()


# ------------------- COMPOSITION (HAS-A RELATIONSHIP) -------------------
class Drawing:
    def __init__(self):
        self.shapes = []  # has-a relationship (composition)

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)


# ------------------- MAIN PROGRAM -------------------
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Rectangle Area:", rect.area())
    print("Rectangle Perimeter:", rect.perimeter())
    print(Rectangle.description())
    print("Is Shape?", Rectangle.is_shape())
    print()

    sq = Square(6)
    print("Square Area:", sq.area())
    print("Square Perimeter:", sq.perimeter())
    print()

    c_sq = ColoredSquare(4, "Blue")
    print(c_sq.display())
    print(c_sq.display(show_area=False))
    print()

    # Composition example
    drawing = Drawing()
    drawing.add_shape(rect)
    drawing.add_shape(sq)
    print("Total Area of Drawing:", drawing.total_area())
