'''

'''


# номер успешной посылки: 34642206

def counting_sort(number_list, digit_place, n):
    output_list = [0 for _ in range(n)]
    count_list = [0 for _ in range(10)]

    for i in range(n):
        index = int((number_list[i] / digit_place))
        count_list[(index) % 10] += 1

    for i in range(1, 10):
        count_list[i] += count_list[i - 1]

    i = n - 1
    while i >= 0:
        index = int((number_list[i] / digit_place))
        output_list[count_list[(index) % 10] - 1] = number_list[i]
        count_list[(index) % 10] -= 1
        i -= 1

    return output_list


def radix_sort(number_list, n):
    max_number = max(number_list)
    digit_place = 1

    while max_number / digit_place >= 1:
        number_list = counting_sort(number_list, digit_place, n)
        digit_place *= 10
    return number_list


if __name__ == "__main__":
    n = int(input())
    number_list = list(map(int, input().split()))
    number = radix_sort(number_list, n)
    print(*number)
