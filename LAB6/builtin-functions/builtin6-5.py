def func(t):
    return all(t)

if __name__ == "__main__":
    user_input = input()
    user_tuple = tuple(map(lambda x: x.lower() == 'true', user_input.split()))
    print("Result:", func(user_tuple))
