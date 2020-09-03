'''
Tom's friends came to visit him. Tom's mother decided to give the kids cookies.
Cookies can be of different sizes. Each child has a greed factor - the minimum
size of cookies that he or she will take. You need to find out how many kids
will be happy to have cookies. Each child can take only one cookie.

Input format
The first line contains the number n - the amount of children.
The second line contains n numbers separated by a space - a greed factor for
each child, an integer number.
The next line contains - m - number of cookies.
Next - m numbers separated by a space - the size of cookies.

Output format
You need to print one number - the number of children who will get cookies.
'''


def cokies(children_amount, greed_level, cookies_amount, cookie_size):
    greed_level.sort()
    cookie_size.sort()
    child = 0
    cookie = 0
    while child < children_amount and cookie < cookies_amount:
        if greed_level[child] <= cookie_size[cookie]:
            child += 1
        cookie += 1
    return child


if __name__ == '__main__':
    children_amount = int(input())
    greed_level = list(map(int, input().split()))
    cookies_amount = int(input())
    cookie_size = list(map(int, input().split()))
    print(cokies(children_amount, greed_level, cookies_amount, cookie_size))
