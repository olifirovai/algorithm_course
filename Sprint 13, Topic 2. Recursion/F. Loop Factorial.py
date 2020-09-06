'''
Find Factorial of Number Using Loop
'''


def factorial(n):
    if n == 1 or n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i

    return result
a = open('input.txt')
b = int(a.readline())
print(factorial(b))