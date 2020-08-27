class MyQueue:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def peek(self):
        if self.is_empty():
            print('None')
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            return x

    def size(self):
        return self.size

    def pop(self):
        if self.is_empty():
            print('None')
        else:
            pass


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
            queue.size()
        elif new_list[m][0] == 'pop':
            queue.pop()
        elif new_list[m][0] == 'peek':
            queue.peek()
        else:
            queue.push(int(new_list[m][1]))


solution()
