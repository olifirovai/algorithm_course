'''
Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.

Input format
The first line contains the number n - the number of matrix rows
In the second - m - number of columns
The following n lines contain m numbers each

Output format
You need to print the matrix elements in a spiral: starting from the upper
left corner to the right.
'''


def decode_message(row_amount, column_amount, matrix):
    starting_row_index = 0
    starting_column_index = 0
    message = []

    while (
            starting_row_index < row_amount and starting_column_index < column_amount):

        for i in range(starting_column_index, column_amount):
            number = matrix[starting_row_index][i]
            message.append(number)
        starting_row_index += 1
        for i in range(starting_row_index, row_amount):
            number = matrix[i][column_amount - 1]
            message.append(number)
        column_amount -= 1
        if (starting_row_index < row_amount):
            for i in range(column_amount - 1, (starting_column_index - 1), -1):
                number = matrix[row_amount - 1][i]
                message.append(number)

            row_amount -= 1
        if (starting_column_index < column_amount):
            for i in range(row_amount - 1, starting_row_index - 1, -1):
                number = matrix[i][starting_column_index]
                message.append(number)
            starting_column_index += 1
    for number in message:
        print(number)


def main():
    n = int(input())
    m = int(input())
    count = 1
    new_list = []
    for _ in range(n):
        new_list.append([])

    while count <= n:
        for k in range(n):
            new_list[k] = list(map(int, input().split()))
            count += 1
    return n, m, new_list


if __name__ == '__main__':
    n, m, new_list = main()
    decode_message(n, m, new_list)
