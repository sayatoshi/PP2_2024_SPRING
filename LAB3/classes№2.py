class Shape:
    def __init__(s):
        s.length = 0

    def area(s):
        return 0

class Square(Shape):
    def __init__(s, length):
        super().__init__()
        s.length = length

    def area(s):
        return s.length * s.length


a = int(input("Enter the length: "))


shape = Shape()
shape.length = a
print("Area of Shape:", shape.area())  
square = Square(a)
print("Area of Square:", square.area())  
