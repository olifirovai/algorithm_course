'''

'''


def f(x, y):
    if y == 0:
        return x
    return f(2*x * y, y - 1)

    print(f(4, 6))