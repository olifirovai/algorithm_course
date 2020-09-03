'''
Jack decided to buy several houses in the mortgage. He found n houses in the
newspaper with their price. Jack can afford a mortgage totaling k dollars.
You need to help Jack figure out how many houses he can buy with this money.

Input format
The first line contains space-separated integers n and k.
n - number of houses that Jack takes a look at
k - total budget

The next line has n house prices written in a space. All prices are integers.

Output format
Print a number equal to the maximum number of houses that Jack can buy.
'''

def main():
    n, k = input().split()
    n, k = int(n), int(k)
    price_list = list(map(int, input().split()))
    price_list.sort()
    sum = 0
    houses = 0
    for i in range(n):
        if price_list[i] <= k and (sum + price_list[i]) <= k:
            sum += price_list[i]
            houses += 1

    print(houses)


if __name__ == '__main__':
    main()
