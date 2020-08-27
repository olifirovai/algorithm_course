'''
Tom decided to confuse his mother by doing things in reverse order. His to-do
list is now stored in a doubly linked list. Write a function that will return
the list in reverse order.
You only need to write a function that takes the head of the doubly linked list
and returns the head of the inverted list.
'''


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def reverse(head):
    tmp = None
    current = head

    while current:
        tmp = current.prev
        current.prev = current.next
        current.next = tmp
        current = current.prev
    if tmp:
        head = tmp.prev
    return head


n5 = DoubleConnectedNode('Fifth to-do thing')
n4 = DoubleConnectedNode('Fourth to-do thing', n5)
n3 = DoubleConnectedNode('Third to-do thing', n4)
n2 = DoubleConnectedNode('Second to-do thing', n3)
n1 = DoubleConnectedNode('First to-do thing', n2)

n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4

reverse(n1)