import re

def func(text):
    pattern = r"([a-z])([A-Z])"
    replaced_text = re.sub(pattern, r"\1 \2", text)
    return replaced_text

input_text = input("Enter a string: ")
result = func(input_text)
print("Result:", result)
