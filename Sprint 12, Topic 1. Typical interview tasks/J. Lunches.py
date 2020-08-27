'''
The management of the company where Tom works gave each employee two coupons
for lunch at a nearby restaurant. Employees could take coupons and write down
their ID number in a special form. Everyone except one employee did so.
You need to find out who it is!
There is a non-empty array of integers. Each of them, except for one, is found
2 times. You need to find out who is not like the others!
'''
from collections import Counter

person_list = list(map(int, input().split()))


def find_person(person_list):
    mydict = Counter(person_list)
    person = [k for k, v in mydict.items() if (v % 2) != 0]
    print(*person)


find_person(person_list)
