'''

'''


def max_photo(capacity_list):
    max_photos = 0
    for number in capacity_list:
        max_photos += number
    return max_photos


def data_center(n, capacity_list, max_photos):
    if n == 0:
        print(max_photos)

    elif n == 1:
        lost_number = capacity_list[0]
        max_photos = (max_photos - lost_number) // 2
        print(max_photos)

    elif len(capacity_list) == 2:
        max_number = max(capacity_list[0], capacity_list[1])
        min_number = min(capacity_list[0], capacity_list[1])
        lost_number = max_number - min_number
        max_photos = (max_photos - lost_number) // 2
        print(max_photos)

    else:
        capacity_list.sort()
        min_number = capacity_list[0]
        max_number = capacity_list[-1]
        prev_max_number = capacity_list[-2]
        operate_number = max_number - prev_max_number
        max_number -= min(min_number, operate_number)
        min_number = max(0, capacity_list[0] - operate_number)
        prev_max_number -= min_number // 2
        max_number -= min_number // 2
        min_number %= 2
        max_number -= min_number
        min_number = 0
        capacity_list[-2] = prev_max_number
        capacity_list[-1] = max_number
        capacity_list[0] = min_number
        capacity_list.sort(reverse=True)
        capacity_list.pop()
        capacity_list.sort()
        data_center(n, capacity_list, max_photos)


n = int(input())
capacity_list = list(map(int, input().split()))

max_photos = max_photo(capacity_list)
data_center(n, capacity_list, max_photos)
