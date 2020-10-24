'''

'''


def data_center(n, capacity_list):
    if n < 2:
        return 0

    photos_amount = 0
    while len(capacity_list) > 1:
        capacity_list.sort()
        capacity_list[-1] -= 1
        capacity_list[0] -= 1
        photos_amount += 1
        if capacity_list[0] == 0:
            capacity_list.pop(0)
        if capacity_list[-1] == 0:
            capacity_list.pop(-1)

    return photos_amount


def main():
    n = int(input())
    capacity_list = list(map(int, input().split()))
    result = data_center(n, capacity_list)
    print(result)


if __name__ == '__main__':
    main()
