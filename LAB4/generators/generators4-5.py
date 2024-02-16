def func(n):
    for i in range(n, -1, -1):
        yield i
a = int(input())
for i in func(a):
    print(i)
