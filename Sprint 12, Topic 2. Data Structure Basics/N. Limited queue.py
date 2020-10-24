'''
Next, Tom needs to write a MyQueueueSized() class that accepts the max_size
parameter, which means the maximum number of elements in the queue.

Input format
The first line contains one number - the number of commands. The second line
contains the maximum allowed queue size Then come the commands, one per line.
Commands can be of the following types:
push x - add number x to the queue
pop - delete a number from the queue and print it
peek - print the first number in the queue
size - return the size of the queue

If the allowed queue size is exceeded, "error" needs to be printed.
When calling the pop operation for an empty queue, you should return None.
If the queue is empty, type None for the peek command.
If the queue is deleted from an empty one, type None.
'''


class MyQueueSized:
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
        else:
            print('error')

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
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            print(x)


def solution():
    amount = int(input())
    n = int(input())
    count = 1
    new_list = []
    for i in range(amount):
        new_list.append(0)
        new_list[i] = []

    queue = MyQueueSized(n)
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


if __name__ == '__main__':
    solution()
