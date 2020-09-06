'''

'''


def max_photo(capacity_list):
    max_photos = 0
    for number in capacity_list:
        max_photos += number
    return max_photos


def data_center(capacity_list, max_photos):
    if len(capacity_list) == 0:
        print(0)
    else:
        if len(capacity_list) > 3:
            capacity_list.sort()
            max_number = capacity_list[-1]
            min_number = capacity_list[0]
            new_number = max_number - min_number
            if new_number != 0:
                capacity_list.pop()
                capacity_list[0] = new_number
                data_center(capacity_list, max_photos)
            else:
                capacity_list.pop()
                capacity_list.sort(reverse=True)
                capacity_list.pop()
                data_center(capacity_list, max_photos)
        elif len(capacity_list) == 3:
            capacity_list.sort()
            a1 = capacity_list[0]
            a2 = capacity_list[1]
            a3 = capacity_list[2]
            operate_number = a3 - a2
            a3 -= min(a1, operate_number)
            a1 = max(0, capacity_list[0] - operate_number)
            a2 -= a1 // 2
            a3 -= a1 // 2
            a1 %= 2
            a3-=a2
            a2 =0
            if a3 == 0:
                max_photos = (max_photos-a1)//2
            else:
                a3 = a3 - a1
                a1 = 0
                max_photos = (max_photos - a3)//2
            # max_photos = (max_photos-max(a1, a3))//2
            print(max_photos)


# n = 5
# capacity_list = [1000, 3000, 2599, 7, 5]
# capacity_list = [8,7,7,6,5]
n = int(input())
capacity_list = list(map(int, input().split()))

max_photos = max_photo(capacity_list)
data_center(capacity_list, max_photos)
# n = int(input())
# capacity_list = list(map(int, input().split()))
