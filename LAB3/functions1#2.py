def convert(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


f_temp = float(input("Enter the temp in F:"))

c_temp = convert(f_temp)

print(f"{f_temp} F = {c_temp:.4f} C")