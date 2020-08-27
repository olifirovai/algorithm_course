'''
Write the function code y = ax^2 + bx + c.
At the input through a space are given numbers a, x, b, c.
'''


def function_value(a, x, b, c):
    y = a * x ** 2 + b * x + c
    print(y)


list_new = list(map(int, input().split()))
a = list_new[0]
x = list_new[1]
b = list_new[2]
c = list_new[3]
function_value(a, x, b, c)