from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def printLevelOrder(root, list=[]):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    level_left = 0
    level_right = 0
    while (len(queue) > 0):
        node = queue.popleft()
        list.append(node.value)

        if node.left is not None:
            queue.append(node.left)
            level_left += 1

        if node.right is not None:
            queue.append(node.right)
            level_right += 1
    if level_right == level_left:
        # print(level_right, level_left)
        n = 1
        k = 0
        f = 1
        a = []
        lengh_range = level_right // 2
        for _ in range(lengh_range + 1):
            new_list = list[k:f]
            a.append(new_list)
            print(f)
            t = n + n
            k = n
            f = n +t
            n+=n

        return a, list
    else:
        return False


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

    a, list = printLevelOrder(root)
    print(a, list)

