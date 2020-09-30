'''
Given a Binary Tree, print left view of it. Left view of a Binary Tree is set
of nodes visible when tree is visited from left side.

Made it the same as C. Genealogical Tree, but print all first elements from
the lists =)
'''

from collections import deque, defaultdict


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    dec = deque()
    result_dict = defaultdict(list)
    dec.appendleft((root, 0))
    result = []

    while dec:
        elem, level = dec.pop()
        result_dict[level].append(elem.value)

        if elem.left:
            dec.appendleft((elem.left, level + 1))

        if elem.right:
            dec.appendleft((elem.right, level + 1))

    for key in sorted(result_dict.keys()):
        result.append(result_dict[key])

    left_view = []
    for i in range(len(result)):
        left_view.append(result[i][0])

    return left_view


if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    root.left.left.right = Node(6)

    root.left.right = Node(3)
    root.left.right.left = Node(6)
    root.left.right.right = Node(5)

    root.right = Node(2)
    root.right.left = Node(3)
    root.right.left.left = Node(5)
    root.right.left.right = Node(6)

    root.right.right = Node(4)
    root.right.right.left = Node(6)
    root.right.right.right = Node(5)

    left_view = solution(root)
    print(left_view)
