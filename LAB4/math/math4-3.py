import math
a=int(input("Input number of sides:"))
b=int(input("Input the length of a side:"))
c=(a*b**2)
pi=180
d = 4 * math.tan(math.pi / a)
area = int(c / d)
print("The area of the polygon is:",area)














