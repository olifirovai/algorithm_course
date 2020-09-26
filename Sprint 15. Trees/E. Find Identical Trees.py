'''
Write Code to Determine if Two Trees are Identical
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def find_twins(root_one, root_two):
    if root_one is None and root_two is None:
        return True

    if root_one is not None and root_two is not None:
        return ((root_one.value == root_two.value) and
                find_twins(root_one.left, root_two.left) and
                find_twins(root_one.right, root_two.right))

    return False


if __name__ == "__main__":
    root_one = Node(122)
    root_one.left = Node(2)
    root_one.right = Node(35)
    root_one.left.left = Node(5)
    root_one.left.right = Node(6)
    root_two = Node(122)
    root_two.left = Node(2)
    root_two.right = Node(35)
    root_two.left.left = Node(5)
    root_two.left.right = Node(6)
    twins = find_twins(root_one, root_two)
    print(twins)
