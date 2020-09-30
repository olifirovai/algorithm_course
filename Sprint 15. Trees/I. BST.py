'''
A program to check if a binary tree is BST or not
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root == None:
        return True

    if root.left != None and root.left.value >= root.value:
        return False

    if root.right != None and root.right.value <= root.value:
        return False

    return solution(root.left) and solution(root.right)


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
    root.right.right.left = Node(7)
    root.right.right.right = Node(5)

    answer = solution(root)
    print(answer)
