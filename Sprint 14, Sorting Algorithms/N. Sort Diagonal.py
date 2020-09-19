'''
Given a m * n matrix mat of integers, sort it diagonally in ascending order
from the top-left to the bottom-right then return the sorted array.
'''


def sort_diagonal(matrix, row, column):
    temp = []

    for r in range(row):
        c = 0
        while r < row and c < column:
            temp.append(matrix[r][c])
            r += 1
            c += 1

        temp.sort()

        while r > 0 and c > 0:
            r -= 1
            c -= 1
            matrix[r][c] = temp.pop()

    for c in range(1, column):
        r = 0
        while r < row and c < column:
            temp.append(matrix[r][c])
            r += 1
            c += 1

        temp.sort()

        while r > 0 and c > 0:
            r -= 1
            c -= 1
            matrix[r][c] = temp.pop()

    return matrix

def main():
    n = int(input())
    m = int(input())
    count = 1
    matrix = []
    for i in range(n):
        matrix.append(0)
        matrix[i] = []

    while count <= n:
        for k in range(n):
            matrix[k] = list(map(int, input().split()))
            count += 1
    return n, m, matrix


if __name__ == '__main__':
    row, column, matrix = main()
    result = sort_diagonal(matrix, row, column)
    for line in result:
        print(*line)

