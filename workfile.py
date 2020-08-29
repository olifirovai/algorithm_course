class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            self.items.pop()

    def adding(self):
        if len(self.items) < 1:
            return None
        self.items[0] = self.items[0] + self.items[1]
        self.items.pop()
        return self.items

    def multiplication(self):
        if len(self.items) < 1:
            return None
        self.items[0] = self.items[0] * self.items[1]
        self.items.pop()
        return self.items

    def subtract(self):
        if len(self.items) < 1:
            return None
        self.items[0] = self.items[0] - self.items[1]
        self.items.pop()
        return self.items

    def division(self):
        if len(self.items) < 1:
            return None
        self.items[0] = self.items[0] // self.items[1]
        self.items.pop()
        return self.items

    def print_stack(self):
        if len(self.items) == 0:
            return None
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])
        print(*self.items)


def make_digits(data):
    for i in range(len(data)):
        try:
            data[i] = int(float(data[i]))
        except ValueError:
            pass
    return data


def stack_calculator():
    stack = Stack()
    input_data = list(map(str, input().split()))
    for element in make_digits(input_data):
        if isinstance(element, int):
            stack.push(element)
        elif element == '+':
            stack.adding()
        elif element == '-':
            stack.subtract()
        elif element == '*':
            stack.multiplication()
        else:
            stack.division()

    return stack.print_stack()


stack_calculator()
