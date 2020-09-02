'''
Reverse Polish Notation Calculator. It is applied to parsing arithmetic
expressions. In contrast to another method used for this problem - using the
operation tree, it is more compact because it does not use brackets.

Input format
A single line contains an expression written in reverse Polish notation.
The numbers and arithmetic operations separated by spaces.
The input may contain the following operations: +, -, *, / and numbers not
exceeding 10000 by module.

Output format
The single number is the value of the expression.
'''

# номер успешной посылки: 33894838

import sys


class StackCalculator:
    def __init__(self):
        self.items = []
        self.action_dict = {'+': 'adding',
                            '-': 'subtract',
                            '*': 'multiplication',
                            '/': 'division',
                            }

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        self.items.pop()

    def adding(self):
        second_operand = self.items.pop()
        first_operand = self.items.pop()
        result = first_operand + second_operand
        self.items.append(result)
        return self.items

    def multiplication(self):
        second_operand = self.items.pop()
        first_operand = self.items.pop()
        result = first_operand * second_operand
        self.items.append(result)
        return self.items

    def subtract(self):
        second_operand = self.items.pop()
        first_operand = self.items.pop()
        result = first_operand - second_operand
        self.items.append(result)
        return self.items

    def division(self):
        second_operand = self.items.pop()
        first_operand = self.items.pop()
        result = first_operand // second_operand
        self.items.append(result)
        return self.items

    def print_stack(self):
        if self.is_empty():
            print('The stack is empty')
        print(*self.items)


def make_digits(data):
    for i in range(len(data)):
        try:
            data[i] = int(float(data[i]))
        except ValueError:
            pass
    return data


def stack_calculator(data, stack):
    for element in data:
        if not stack.action_dict.get(element):
            stack.push(element)
        else:
            function_name = stack.action_dict.get(element)
            this_module = sys.modules[__name__]
            func = getattr(this_module, function_name)
            func()
    return stack.print_stack()


def main():
    input_data = list(map(str, input().split()))
    data = make_digits(input_data)
    stack = StackCalculator()
    stack_calculator(data, stack)


if __name__ == '__main__':
    main()
