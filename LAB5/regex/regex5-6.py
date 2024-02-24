import re

def func(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

input_text = input("Enter a string: ")
result = func(input_text)
print("Result:", result)
