'''
Two numbers are given in the binary system. You need to output their sum,
but also in the binary system. Built-in in the programming language the option
of adding binary numbers can not be used.
The solution should work for O(n) and use O(n) additional memory, where N
is the number of digits of the maximum number at the input.
'''

number_one = list(map(int, str(input())))[::-1]
number_two = list(map(int, str(input())))[::-1]


def sum_numbers(number_one, number_two):
    c = []
    d = len(number_one) - len(number_two)
    if d > 0:
        for k in range(d):
            number_two.append(0)
    elif d < 0:
        for l in range(-d):
            number_one.append(0)
    for j in range(max(len(number_one), len(number_two)) + 1):
        c.append(0)
    for i in range(len(number_one)):
        c[i] = (int(c[i])) + (int(number_one[i])) + (int(number_two[i]))
        if c[i] == 2:
            c[i] = 0
            c[i + 1] = 1
        elif c[i] == 3:
            c[i] = 1
            c[i + 1] = 1
    if c[::-1][0] == 0:
        c.pop()

    print(''.join(map(str, c[::-1])))


sum_numbers(number_one, number_two)
