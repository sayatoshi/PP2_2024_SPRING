def convert(degrees):
    radian=degrees/57.2958
    return radian

degrees= float(input("Enter the number of degrees:"))

result = convert(degrees)

print(result)