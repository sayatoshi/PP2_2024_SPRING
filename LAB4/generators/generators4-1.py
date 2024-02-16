def func(n):
    for i in range(1, n+1):
        yield i**2

a = int(input())
b = func(a)
for j in b:
    print(j)
