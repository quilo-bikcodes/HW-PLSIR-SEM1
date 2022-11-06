def gen_func(x):
    for i in range(x):
        yield i

y = gen_func(3)

print(next(y))
print(next(y))
