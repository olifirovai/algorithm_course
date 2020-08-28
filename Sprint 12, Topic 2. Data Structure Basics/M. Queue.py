'''
Tom faces the challenge of writing several releases of his own queue, as the
options available on the market are not suitable for the project. The
requirements to the first one are as follows: the class must be called
MyQueueue(), it should support operations of adding, deleting, getting an
element, defining the current size, and a method showing whether the queue is
empty or not. The data structure must be based on an array.

Input format
The first line contains one number - the number of commands. Then come the
commands, one per line. Commands can be of the following types:
push x - add number x to the queue
pop - delete a number from the queue and print it
peek - print the first number in the queue
size - return the size of the queue

When calling the pop operation for an empty queue, you should return None.
If the queue is empty, type None for the peek command.
If the queue is deleted from an empty one, type None.
'''



class MyQueue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        self.queue.append(x)
        self.tail = self.tail + 1
        self.size += 1

    def peek(self):
        if self.is_empty():
            print('None')
        else:
            x = self.queue[self.head]
            print(x)

    def get_size(self):
        print(self.size)

    def pop(self):
        if self.is_empty():
            print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = self.head + 1
            self.size -= 1
            print(x)


def solution():
    amount = int(input())
    count = 1
    new_list = []
    for i in range(amount):
        new_list.append(0)
        new_list[i] = []

    queue = MyQueue()
    while count <= amount:
        for k in range(amount):
            new_list[k] = list(map(str, input().split()))
            count += 1
    for m in range(amount):
        if new_list[m][0] == 'size':
            queue.get_size()
        elif new_list[m][0] == 'pop':
            queue.pop()
        elif new_list[m][0] == 'peek':
            queue.peek()
        else:
            queue.push(int(float(new_list[m][1])))


solution()
