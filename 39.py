def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y = yrange(3)

print(next(y))
print(next(y))