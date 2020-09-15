'''

'''
# номер успешной посылки: 34481438

def data_center(n, capacity_list, max_photos):
    if n < 2:
        return 0

    while len(capacity_list) > 1:
        capacity_list.sort()
        max_number = capacity_list[-1]
        min_number = capacity_list[0]
        capacity_list[-1] = max_number - 1
        capacity_list[0] = min_number - 1

        if capacity_list[0] == 0:
            capacity_list.pop(0)
        if capacity_list[-1] == 0:
            capacity_list.pop(-1)

    if len(capacity_list) == 1:
        max_photos = (max_photos - capacity_list[0]) // 2
        return max_photos

    return (max_photos // 2)


def main():
    n = int(input())
    capacity_list = list(map(int, input().split()))
    max_photos = sum(capacity_list)
    result = data_center(n, capacity_list, max_photos)
    print(result)


if __name__ == '__main__':
    main()
