'''


'''


# номер успешной посылки: 34475228


def find_bourder(left_side, right_side, number_list):
    midlle = (left_side + right_side) // 2

    if right_side - left_side > 1:
        if number_list[midlle] > number_list[right_side]:
            left_side = midlle
            return find_bourder(left_side, right_side, number_list)
        right_side = midlle
        return find_bourder(left_side, right_side, number_list)
    return left_side, right_side


def binary_search(left_point, right_point, number_list, find_number):
    if left_point <= right_point:
        midlle = (right_point + left_point) // 2
        if number_list[midlle] < find_number:
            left_point = midlle + 1
            return binary_search(left_point, right_point, number_list,
                                 find_number)
        if number_list[midlle] > find_number:
            right_point = midlle - 1
            return binary_search(left_point, right_point, number_list,
                                 find_number)
        return midlle
    return -1


def find_index(find_number, number_list):
    left_side = 0
    right_side = len(number_list) - 1
    if number_list[left_side] < number_list[right_side]:
        return binary_search(left_side, right_side, number_list, find_number)
    left_point, right_point = find_bourder(left_side, right_side,
                                           number_list)
    if (find_number >= number_list[left_side] and find_number
            <= number_list[left_point]):
        return binary_search(left_side, left_point, number_list, find_number)
    return binary_search(right_point, right_side, number_list, find_number)


def main():
    len_list = int(input())
    find_number = int(input())
    number_list = list(map(int, input().split()))

    result = find_index(find_number, number_list)
    print(result)


if __name__ == '__main__':
    main()
