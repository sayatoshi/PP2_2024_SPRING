def func(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
a = func(n)
result = ','.join(map(str, a))
print(result)
