def func(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper() and snake_case:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

camel_case_input = input("Enter a camelCase string: ")
snake_case_output = func(camel_case_input)
print("snake_case:", snake_case_output)
