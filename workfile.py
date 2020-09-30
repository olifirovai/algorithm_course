'''

'''
import heapq

WIN = ['k', 'o', 'n', 'd', 'r', 'a', 't', 'i', 'y']


class Rider:
    def __init__(self, rider):
        self.rider = rider

    def name(self):
        for name in self.rider[:1]:
            return name

    def is_kondrat(self):
        new_list = WIN
        for letter in self.name():
            if letter in new_list:
                new_list.remove(letter)

        if not new_list:
            return True
        return False

    def points(self):
        point_list = self.rider[1:]
        points = sum([int(item) for item in point_list if int(item) > 0])
        return points
    #
    # def __gt__(x, y):
    #
    #     if not x.is_kondrat() and not y.is_kondrat():
    #         if x.points() == y.points():
    #             return x.name() < y.name()
    #         return x.points() > y.points()
    #
    #     if x.is_kondrat() and y.is_kondrat():
    #         return x.is_kondrat() == y.is_kondrat()
    #     return x.is_kondrat() > y.is_kondrat()

    # def __lt__(x, y):
    #
    #     if not x.is_kondrat() or y.is_kondrat():
    #         if x.points() == y.points():
    #             return x.name() > y.name()
    #         return x.points() < y.points()
    #
    #     if x.is_kondrat() and y.is_kondrat():
    #         return False
    #     return x.is_kondrat() < y.is_kondrat()

    # def __gt__(x, y):
    #     if x.is_kondrat() and y.is_kondrat():
    #         return True
    #
    #     if x.is_kondrat() or y.is_kondrat():
    #         return x.is_kondrat() > y.is_kondrat()
    #
    #     if x.points() == y.points():
    #         return x.name() < y.name()
    #     return x.points() > y.points()

    def __lt__(x, y):
        return x.name() > y.name()


    # def __lt__(x, y):
    #     if x.is_kondrat() and y.is_kondrat():
    #         return False
    #
    #     if x.is_kondrat() or y.is_kondrat():
    #         return x.is_kondrat() < y.is_kondrat()
    #
    #     if x.points() == y.points():
    #         return x.name() > y.name()
    #     return x.points() < y.points()


# rider_name = 'kondcvhxfghdsfratiy'
# print(kondratiy(rider_name))
# rider_list = ['12', '11', '13', '5', '6', '7']
# points = sum([item for item in rider_list[1:] if int(item) > 0])
#
#
class Comparator_kondrat(str):

    def __gt__(x, y):

        return x.is_kondrat() > y.is_kondrat()

class Comparator_points(str):

    def __gt__(x, y):
        return x.points() > y.points()

# if x.is_kondrat() and y.is_kondrat():
#     return True
#
# if x.is_kondrat() or y.is_kondrat():
#     return x.is_kondrat() > y.is_kondrat()
#
# if x.points() == y.points():
#     return x.name() < y.name()
# return x.points() > y.points()


def heapify(rider_list, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and rider_list[i] < rider_list[left_child]:
        largest = left_child

    if right_child < n and rider_list[largest] < rider_list[right_child]:
        largest = right_child

    if largest != i:
        rider_list[i], rider_list[largest] = rider_list[largest], rider_list[i]

        heapify(rider_list, n, largest)


def heapSort(rider_list, n):
    parent = (n - 1) // 2
    for i in range(parent, -1, -1):
        heapify(rider_list, n, i)

    for i in range(n - 1, 0, -1):
        rider_list[i], rider_list[0] = rider_list[0], rider_list[i]
        heapify(rider_list, i, 0)


if __name__ == "__main__":
    rider_list = []

    # n = int(input())
    # for _ in range(n):
    #     rider = Rider(list(map(str, input().split())))
    #     rider_list.append(rider)
    rider4 = Rider(['ands', '1', '9', '5', '-1', '1'])
    rider_list.append(rider4)

    rider5 = Rider(['kondratiy', '0', '2', '5', '0', '-1'])
    rider_list.append(rider5)

    rider6 = Rider(['kondratiy', '0', '1', '5', '0', '-1'])
    rider_list.append(rider6)

    rider7 = Rider(['kondrafssdtiy', '0', '0', '5', '0', '-1'])
    rider_list.append(rider7)

    rider1 = Rider(['anna', '2', '-4', '5', '0', '1'])
    rider_list.append(rider1)

    rider2 = Rider(['sam', '1', '9', '5', '0', '1'])
    rider_list.append(rider2)

    rider3 = Rider(['ands', '1', '9', '5', '0', '1'])
    rider_list.append(rider3)


    # 'kondrafssdtiy', '0', '0', '5', '0', '-1'
    # 'kondratiy', '0', '1', '5', '0', '-1'
    # 'kondratiy', '0', '2', '5', '0', '-1'
    # 'ands', '1', '9', '5', '-1', '1'
    # 'ands', '1', '9', '5', '0', '1'
    # 'sam', '1', '9', '5', '0', '1'
    # 'anna', '1', '-4', '5', '0', '1'

    #
    lenght = len(rider_list)
    heapq.heapify(rider_list)
    # heapSort(rider_list, lenght)
    sorted_rider_list = (sorted(rider_list, key=Comparator_points))

    sorted_rider_list = (sorted(rider_list, key=Comparator_kondrat))
    for rider in rider_list:
        print(*rider.rider)
