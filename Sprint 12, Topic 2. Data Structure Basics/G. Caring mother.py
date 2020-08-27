'''
Tom's mother wants to know what her son plans to do and when.
Help her: Write the solution function that defines the index of the first
occurrence of the value sent to her in the linked list if the value is present.
We need to write only the function that takes the head and the searched item
and returns an integer number - the index of the found item or -1.
'''

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value



def solution(node, value):
    head = node
    index = 0
    try:
        while head.value != value:
            head = head.next_item
            index += 1
        return index
    except AttributeError:
        return -1

n5 = Node('Fifth to-do thing')
n4 = Node('Fourth to-do thing', n5)
n3 = Node('Third to-do thing', n4)
n2 = Node('Second to-do thing', n3)
n1 = Node('First to-do thing', n2)

node, value = n1,'Third to-do thing'
print(solution(node, value))