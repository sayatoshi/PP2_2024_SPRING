def func(n):
    for i in range(1, n+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

a = int(input())
b = func(a)

for j in b:
    print(j)
