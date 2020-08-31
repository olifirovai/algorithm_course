'''
Write a function hasCycle() that checks whether a given Linked List contains
loop and if loop is present then removes the loop and returns True.
If the list doesn’t contain loop then it returns False.
'''

#номер успешной посылки: 33954495

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(node):
    if node is None:
        return False
    one_step = node
    two_step = node
    while (one_step and two_step and two_step.next):
        one_step = one_step.next
        two_step = two_step.next.next
        if one_step == two_step:
            return True
    return False
