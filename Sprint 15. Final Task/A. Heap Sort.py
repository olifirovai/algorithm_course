'''

'''
import heapq

WINNER = 'kondratiy'


class ConfigurateRiderInfo:

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


def configurate_rider(n):
    sourse_rider = []
    rider_heap = []

    for _ in range(n):
        rider = list(map(str, input().split()))
        sourse_rider.append(rider)

    index = 0
    for rider in sourse_rider:
        driver_sheet = ConfigurateRiderInfo(rider)
        rider_kondrat = driver_sheet.is_kondrat()
        rider_points = driver_sheet.points()
        rider_name = driver_sheet.name()
        single_rider = RiderInfo(index, rider_kondrat, rider_points,
                                 rider_name, rider)
        heapq.heappush(rider_heap, single_rider)
        index += 1

    return rider_heap


if __name__ == "__main__":
    n = int(input())

    rider_heap = configurate_rider(n)
    heapSort(rider_heap, n)

    for rider in reversed(rider_heap):
        print(*rider.full_info)
