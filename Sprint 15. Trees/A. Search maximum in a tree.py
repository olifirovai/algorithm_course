class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value


def solution(node):
    if node.left is None and node.right is None:
        return node.value
    if node.left is None and node.right is not None:
        return max(node.value, solution(node.right))
    if node.left is not None and node.right is None:
        return max(node.value, solution(node.left))
    return max(node.value, solution(node.left), solution(node.right))


if __name__ == "__main__":
    root = Node(-654621)
    root.left = Node(-299999999)
    root.right = Node(-35)
    root.left.left = Node(-4)
    root.left.right = Node(-5)
    root.right.left = Node(-25)
    root.right.right = Node(-7)
    root.right.left.left = Node(-8)
    root.right.left.right = Node(-54651)
    root.right.right.right = Node(-10)

    maximum = solution(root)
    print(maximum)
