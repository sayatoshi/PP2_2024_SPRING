def func(snake_case):
    words = snake_case.split('_')
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case = ''.join(camel_case_words)
    return camel_case

snake_case_input = input("Enter a snake_case string: ")
camel_case_output = func(snake_case_input)
print("CamelCase:", camel_case_output)
