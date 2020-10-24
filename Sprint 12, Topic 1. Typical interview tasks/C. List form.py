'''
For a non-negative integer X, the list form is an array of its digits from left
to right. For example, for 1231 the list form will be [1,2,3,1]. The input is
given the number of digits of number X, the list form of non-negative number
X and number K. Numbers K and X do not exceed 10000.
You need to return the list form of numbers X + K.

The first line is the length of the list form of number X. The next line is the
list form itself with numbers written through a space. The last line contains
the number K.
'''


def list_form(form_len, form, k):
    form = int(form[:form_len])
    sum = " ".join(str(form + k))
    print(sum)


def main():
    form_len = int(input())
    form = input().replace(" ", "")
    k = int(input())
    list_form(form_len, form, k)


if __name__ == '__main__':
    main()
