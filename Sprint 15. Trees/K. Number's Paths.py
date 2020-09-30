'''
Given a binary tree, where every node value is a Digit from 1-9. Find the sum
of all the numbers which are formed from root to leaf paths.

'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root, val=0):
    if root is None:
        return 0

    val = (val * 10 + root.value)

    if root.left is None and root.right is None:
        return val

    result = (solution(root.left, val) + solution(root.right, val))

    return result


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

    result = solution(root, 0)
    print(result)
