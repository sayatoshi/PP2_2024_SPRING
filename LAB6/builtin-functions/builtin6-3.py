def func(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    inpput = input("Enter a string: ")
    if func(inpput):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
