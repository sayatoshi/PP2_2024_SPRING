class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = int(input("Enter the Length: "))
width = int(input("Enter the Width: "))

rectangle = Rectangle(length, width)
print("Area of Rectangle:", rectangle.area())
