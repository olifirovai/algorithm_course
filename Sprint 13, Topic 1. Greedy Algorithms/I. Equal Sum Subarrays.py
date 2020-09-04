'''

'''
n = int(input())
a = list(map(int, input().split()))
# a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 19]
# n = len(a)
a.sort()


#
def find_equal_sum(arr, n):
    left_sum = 0
    right_sum = 0
    sum_all = 0
    arr.sort()
    for i in range(0, n):
        sum_all += arr[i]
    if n > 1 and (sum_all % 2) == 0:
        for i in range(0, n):
            left_sum += arr[i]

        for i in range(n - 1, -1, -1):
            right_sum += arr[i]
            left_sum -= arr[i]

            if (right_sum == left_sum):
                return True
    return False


print(find_equal_sum(a, n))

#
# def findSplitPoint(arr, n):
#     left_sum = 0
#     if n > 1:
#         for i in range(0, n):
#             left_sum += arr[i]
#
#             right_sum = 0
#             for j in range(i + 1, n):
#                 right_sum += arr[j]
#             if (left_sum == right_sum):
#                 return True
#     return False
#
#
# print(findSplitPoint(a, n))
