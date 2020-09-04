'''
Find Factorial of Number Using Recursion
'''


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


# a = open('input.txt')
# b = int(a.readline())
print(factorial(6))
