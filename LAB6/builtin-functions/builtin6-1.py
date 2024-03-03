from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers_list = [1, 2, 3, 4, 5]
result = multiply_list(numbers_list)
print("Result of multiplying all numbers in the list:", result)
