#11111111111111111111
import math

def func(n):
    pi_number = str(math.pi)
    
    if n <= len(pi_number):
        return pi_number[n]

n = int(input("Введите позицию N: "))
print(f"Цифра числа π на позиции {n}:", func(n))


#2222222222222222222
from datetime import datetime, timedelta

input_date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

new_date = input_date + timedelta(days=56)

print("Через год после", input_date_str, "будет", new_date.strftime("%Y-%m-%d"))


#3333333333333333333333333
import math

def func(n):
    pi_number = str(math.pi)
    print("Цифры числа π до позиции", n, ":")
    print(pi_number[:n])

n = int(input("Введите позицию N: "))
func(n)



#44444444444444444444444444444

input_str1 = input("Введите цифры первого списка через пробел: ")
list1 = list(map(int, input_str1.split()))

input_str2 = input("Введите цифры второго списка через пробел: ")
list2 = list(map(int, input_str2.split()))

result = list(map(lambda x, y: x * y, list1, list2))

print(result)
