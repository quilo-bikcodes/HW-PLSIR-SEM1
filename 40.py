def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1
def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        print("Loop Ended")
    return result

print(take(5, squares())) 