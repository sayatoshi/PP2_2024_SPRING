def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    upper, lower = count_upper_lower(input_string)
    print("Number of uppercase letters:", upper)
    print("Number of lowercase letters:", lower)
