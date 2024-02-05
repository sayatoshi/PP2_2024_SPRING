import math

def svolume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume


radius = float(input("Enter the radius of the sphere: "))
result = svolume(radius)
print(f"The volume of the sphere with radius {radius} is: {result:.1f} ")
