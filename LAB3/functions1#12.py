def histogram(numbers):
    for num in numbers:
        print("*" * num)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

histogram([a, b, c])
