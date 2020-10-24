'''
Tom thinks about what not to do from the list.
But it seems that all things are very important! Tom decides to guess the
number and delete the thing that goes with this number.
The list of to-do is presented as a singly linked list.
Write the solution function, which takes the head of the list and the number
of the case to be deleted and returns the head of the updated list.
'''


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node, index):
    head = node
    if index == 0:
        head = node.next_item
        return head
    head_index = 0
    while head_index < index - 1:
        head = head.next_item
        head_index += 1
    next = head.next_item.next_item
    head.next_item = None
    head.next_item = next
    return head


n5 = Node('Fifth to-do thing')
n4 = Node('Fourth to-do thing', n5)
n3 = Node('Third to-do thing', n4)
n2 = Node('Second to-do thing', n3)
n1 = Node('First to-do thing', n2)

node, index = n1, 2

if __name__ == '__main__':
    print(solution(node, index))
