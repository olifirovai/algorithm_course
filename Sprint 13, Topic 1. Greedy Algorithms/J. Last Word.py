'''
You need to print the length of the last word in the given string
'''


def main():
    words_list = list(map(str, input().split()))

    print(len(words_list[-1]))


if __name__ == '__main__':
    main()
