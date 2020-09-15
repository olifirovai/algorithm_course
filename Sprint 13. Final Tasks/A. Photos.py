'''

'''


def data_center(n, capacity_list, max_photos):
    if n < 2:
        return 0

    while len(capacity_list) > 2:
        '''
        This algorithm provides distribution of the smaller element between the
        bigger two so that the bigger two elements will be maximally leveled 
        between each other. It decreases the largest element until it is equal
        to the second element. Next it decreases the bigger two elements 
        equally. In this way they are evenly reduced. If the size of the 
        smaller element is not enough to equalize the larger two elements with
        each other, the smaller element just reduces the largest element.
        '''
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
        capacity_list.pop(min_number)

    if len(capacity_list) == 2:
        max_number = max(capacity_list[0], capacity_list[1])
        min_number = min(capacity_list[0], capacity_list[1])
        lost_number = max_number - min_number
        max_photos = (max_photos - lost_number) // 2
        return max_photos


def main():
    n = int(input())
    capacity_list = list(map(int, input().split()))
    max_photos = sum(capacity_list)
    result = data_center(n, capacity_list, max_photos)
    print(result)


if __name__ == '__main__':
    main()
