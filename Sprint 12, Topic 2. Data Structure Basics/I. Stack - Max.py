'''
You need to realize the StackMax class, which supports the operation of
defining the maximum among all elements in the stack. The class must also
support push and pop operations.

Input format:
The first line contains n - the number of commands. In the next n lines are
given the commands. Commands can be of the following types:
push x - add number x to the stack
pop - remove the number from the top of the stack
get_max - print maximum number in stack

If the stack is empty when you call the get_max command, you need to
type None, for the pop command - error.
'''


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
        else:
            print(max(self.items))


def solution():
    amount = int(input())
    count = 1
    new_list = []
    for i in range(amount):
        new_list.append(0)
        new_list[i] = []

    stack = StackMax()
    while count <= amount:
        for k in range(amount):
            new_list[k] = list(map(str, input().split()))
            count += 1
    for m in range(amount):
        if new_list[m][0] == 'get_max':
            stack.get_max()
        elif new_list[m][0] == 'pop':
            stack.pop()
        else:
            stack.push(int(new_list[m][1]))


if __name__ == '__main__':
    solution()
