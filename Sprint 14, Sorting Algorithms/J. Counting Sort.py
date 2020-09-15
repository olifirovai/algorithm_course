'''


'''
n = int(input())
try:
    list_a = list(map(int, input().split()))
except EOFError:
    list_a = ''
k = int(input())
try:
    list_b = list(map(int, input().split()))
except EOFError:
    list_b = ''


def sort_given_order(k, list_a, list_b):
    list_c = [0 for _ in range(k)]
    for i in range(k):
        list_c[i] = list_a.count(list_b[i])

    for i in range(1, k):
        list_c[i] += list_c[i - 1]

    index = 0
    output_list = [0 for _ in range(list_c[-1])]
    for i in range(0, list_c[-1]):
        if i < list_c[index]:
            output_list[i] = list_b[index]
            list_a.remove(output_list[i])
        elif i == list_c[index]:
            output_list[i] = list_b[index + 1]
            list_a.remove(output_list[i])
            index += 1

        elif index == list_c[-1]:
            break

    return output_list


def left_sort(list_a):
    max_element = int(max(list_a))
    min_element = int(min(list_a))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(list_a))]

    for i in range(0, len(list_a)):
        count_arr[list_a[i] - min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(list_a) - 1, -1, -1):
        output_arr[count_arr[list_a[i] - min_element] - 1] = list_a[i]
        count_arr[list_a[i] - min_element] -= 1

    for i in range(0, len(list_a)):
        list_a[i] = output_arr[i]

    return list_a


if n != 0 and k != 0:
    output_list = sort_given_order(k, list_a, list_b)
    new_list_a = left_sort(list_a)
    print(*(output_list + new_list_a))

elif n == 0:
    print('')
else:
    new_list_a = left_sort(list_a)
    print(*new_list_a)
