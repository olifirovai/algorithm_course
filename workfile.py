'''

'''


def main():
    children_amount = int(input())
    greed_level = list(map(int, input().split()))
    cookies_amount = int(input())
    cookie_size = list(map(int, input().split()))
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
    print(main())
