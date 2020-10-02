'''

'''
import heapq

WINNER = 'kondratiy'


# class Rider:
#     def __init__(self, rider):
#         self.rider = rider
#
#     def name(self):
#         for name in self.rider[:1]:
#             return name
#
#     def is_kondrat(self):
#         new_list = WIN
#         for letter in self.name():
#             if letter in new_list:
#                 new_list.remove(letter)
#
#         if not new_list:
#             return True
#         return False
#
#     def points(self):
#         point_list = self.rider[1:]
#         points = sum([int(item) for item in point_list if int(item) > 0])
#         return points
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

# def __gt__(x, y):
#     return x.is_kondrat() > y.is_kondrat()
#
#
# def __lt__(x, y):
#     return x.name() > y.name()


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


# class Comparator_kondrat(str):
#
#     def __gt__(x, y):
#         return x.is_kondrat() > y.is_kondrat()
#
#
# class Comparator_points(str):
#
#     def __gt__(x, y):
#         return x.points() > y.points()


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


class GenerateeRiderInfo:

    def __init__(self, rider):
        self.rider = rider

    def is_kondrat(self):
        win_name = set(WINNER)
        rider_name = set(self.rider[0])

        return win_name <= rider_name

    def points(self):
        point_list = self.rider[1:]
        points = sum([int(item) for item in point_list if int(item) > 0])
        return points

    def name(self):
        name = self.rider[:1]
        return name


# class Comparator(str):
#
#     def __gt__(x, y):
#         return x.points > y.points

class RiderInfo:

    def __init__(self, index, is_kondrat, points, name, full_info):
        self.index = index
        self.is_kondrat = is_kondrat
        self.points = points
        self.name = name
        self.full_info = full_info

    def __lt__(x, y):
        if x.is_kondrat and y.is_kondrat:
            return x.index < y.index

        if x.is_kondrat or y.is_kondrat:
            return x.is_kondrat < y.is_kondrat

        if not (x.is_kondrat and y.is_kondrat):
            if x.points == y.points:
                if x.name == y.name:
                    return x.index < y.index
                return x.name > y.name
            return x.points < y.points

    # def __lt__(x, y):
    #     if x.points == y.points:
    #         if x.name == y.name:
    #             return x.index < y.index
    #         return x.name > y.name
    #     return x.points < y.points


if __name__ == "__main__":
    sourse_rider=[]
    n = int(input())
    for _ in range(n):
        rider = list(map(str, input().split()))
        sourse_rider.append(rider)

    # sourse_rider = [['1kondratiy', '1', '9', '5', '0', '-1'],
    #                 ['anna', '1', '-4', '5', '0', '1', '-6', '-7'],
    #                 ['sam', '1', '9', '5', '0', '1', '-4', '-16'],
    #                 ['2kondratiy', '1', '9', '5', '0', '-1'],
    #                 ['3kondratiy', '1', '9', '5', '0', '-1'],
    #                 ['sam', '1', '9', '5', '0', '1', '-3', '-16'],
    #                 ['sam', '1', '9', '5', '0', '2', '-1', '-17'],
    #                 ['anna', '1', '-4', '5', '0', '1', '-5', '-7'],
    #                 ['anna', '1', '9', '5', '0', '1', '-2', '-16']]
    rider_heap = []
    index = 0
    for rider in sourse_rider:
        driver_sheet = GenerateeRiderInfo(rider)
        rider_kondrat = driver_sheet.is_kondrat()
        rider_points = driver_sheet.points()
        rider_name = driver_sheet.name()
        single_rider = RiderInfo(index, rider_kondrat, rider_points,
                                 rider_name, rider)
        heapq.heappush(rider_heap, single_rider)
        # if rider_kondrat:
        #     heapq.heappush(kongrat_heap, single_rider)
        # else:
        #     heapq.heappush(rider_heap, single_rider)
        index += 1

        # rider_list.append(single_rider)

    # '3kondratiy', '1', '9', '5', '0', '-1'
    # '2kondratiy', '1', '9', '5', '0', '-1'
    # '1kondratiy', '1', '9', '5', '0', '-1'
    # 'sam', '1', '9', '5', '0', '2', '-1'   - 17
    # 'anna', '1', '9', '5', '0', '1'        - 16
    # 'sam', '1', '9', '5', '0', '1', '-1'   - 16
    # 'sam', '1', '9', '5', '0', '1', '-2'   - 16
    # 'anna', '1', '-4', '5', '0', '1', '-1' - 7
    # 'anna', '1', '-4', '5', '0', '1', '-2' - 7

    # lenght = len(rider_heap)
    # heapq.heapify(rider_heap)
    heapSort(rider_heap, n)
    # sorted_rider_list = (sorted(rider_list, key=Comparator_points))
    #
    # for i in range(len(rider_heap)):
    #     rider_heap[i].sort(key=Comparator)
    # for _ in range(len(kongrat_heap)):
    #     print(*heapq.heappop(kongrat_heap).full_info)

    # print('-----------')
    # new_rider_list = reversed(sorted(rider_heap, key=lambda x: (x[1].points)))
    # for _ in range(len(rider_heap)):
    #     print(heapq.heappop(rider_heap)[1].full_info)
    for rider in reversed(rider_heap):
        print(*rider.full_info)
