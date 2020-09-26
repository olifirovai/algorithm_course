'''

'''


# номер успешной посылки: 34868773

def radix_sort(number_list):
    max_number = max(number_list)
    digit_place = 1

    lists_list = []
    for _ in range(10):
        lists_list.append([])

    while max_number / digit_place >= 1:
        for number in number_list:
            list_index = (number // digit_place) % 10
            lists_list[list_index].append(number)

        number_list.clear()
        for single_list in lists_list:
            number_list.extend(single_list)
            single_list.clear()

        digit_place *= 10

    return number_list


if __name__ == "__main__":
    n = int(input())
    number_list = list(map(int, input().split()))
    number = radix_sort(number_list)
    print(*number)
