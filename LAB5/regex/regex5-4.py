import re

def func(text):
    pattern = r"[A-Z][a-z]+"
    if re.fullmatch(pattern, text):
        print("The string matches the pattern.")
    else:
        print("The string does not matches the pattern.")

text = input("Input string: ")
func(text)