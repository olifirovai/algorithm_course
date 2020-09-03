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


# номер успешной посылки: 33992198

class StackCalculator:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        self.items.pop()

    def adding(self, first_operand, second_operand):
        result = first_operand + second_operand
        self.items.append(result)
        return self.items

    def multiplication(self, first_operand, second_operand):
        result = first_operand * second_operand
        self.items.append(result)
        return self.items

    def subtract(self, first_operand, second_operand):
        result = first_operand - second_operand
        self.items.append(result)
        return self.items

    def division(self, first_operand, second_operand):
        result = first_operand // second_operand
        self.items.append(result)
        return self.items

    def stack_calculator(self, data):
        action_dict = {'+': self.adding,
                       '-': self.subtract,
                       '*': self.multiplication,
                       '/': self.division,
                       }
        for element in data:
            if not action_dict.get(element):
                self.push(element)
            else:
                second_operand = self.items.pop()
                first_operand = self.items.pop()
                action_dict[element](first_operand, second_operand)
        return self.peak()

    def peak(self):
        if self.is_empty():
            print('The stack is empty')
        print(self.items[-1])


def make_digits(data):
    for i in range(len(data)):
        try:
            data[i] = int(float(data[i]))
        except ValueError:
            pass
    return data


def main():
    input_data = list(map(str, input().split()))
    data = make_digits(input_data)
    stack = StackCalculator()
    stack.stack_calculator(data)


if __name__ == '__main__':
    main()
