def foo():
    print("begin")
    for i in range(3):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")

f=foo()

print(next(f))
print(next(f))
print(next(f))

