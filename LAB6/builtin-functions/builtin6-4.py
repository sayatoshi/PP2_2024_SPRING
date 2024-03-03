import time
import math

def func(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")

if __name__ == "__main__":
    number = int(input())
    milliseconds = int(input())
    func(number, milliseconds)
