'''
Tom decided to remove from the statistics the days when nothing in the online
game has earned or lost. Here is a list of points earned. You need to remove
zeroes from it. You can't use any more memory than O(1).
'''


def remove_zeros(c, a):
    b = [x for x in a if x != 0]
    print(*b)

c = int(input())
a = list(map(int, input().split()))
remove_zeros(c, a)