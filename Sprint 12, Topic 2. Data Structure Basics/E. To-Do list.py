'''
Tom needs to print out his to-do list for today.
Help him: Write a function that prints all his stuff.
It is known that Tom has no more than 5000 things to do.
'''


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node):
    while node:
        print(node)
        node = node.next_item


n5 = Node('Fifth to-do thing')
n4 = Node('Fourth to-do thing', n5)
n3 = Node('Third to-do thing', n4)
n2 = Node('Second to-do thing', n3)
n1 = Node('First to-do thing', n2)

node = n1
head = solution(node)
