'''

'''


def counting_sort(arr, exp, n):
    output_list = [0 for _ in range(n)]
    count_list = [0 for _ in range(10)]

    for i in range(0, n):
        index = int((arr[i] / exp))
        count_list[(index) % 10] += 1

    for i in range(1, 10):
        count_list[i] += count_list[i - 1]

    i = n - 1
    while i >= 0:
        index = int((arr[i] / exp))
        output_list[count_list[(index) % 10] - 1] = arr[i]
        count_list[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output_list[i]


def radixSort(number_list, n):
    max_number = max(number_list)
    exp = 1

    while max_number / exp > 1:
        counting_sort(number_list, exp, n)
        exp *= 10
    return number_list


if __name__ == "__main__":
    n = int(input())
    number_list = list(map(int, input().split()))
    number = radixSort(number_list, n)
    print(*number)


# 2 98545 365 9578 99999 62545 5124 32