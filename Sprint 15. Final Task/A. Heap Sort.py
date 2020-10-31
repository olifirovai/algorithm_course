'''

'''

import heapq

WINNER = 'kondratiy'


class RiderInfo:

    def __init__(self, rider, index):
        self.rider = rider
        self.index = index
        self.is_kondrat = self.is_kondratiy(rider)
        self.points = self.rider_points(rider)
        self.name = self.rider_name(rider)

    def __str__(self):
        return (' '.join(self.rider))

    @classmethod
    def is_kondratiy(self, rider):
        win_name = set(WINNER)
        rider_name = set(rider[0])

        return win_name.issubset(rider_name)

    @classmethod
    def rider_points(self, rider):
        point_list = rider[1:]
        points = sum([int(item) for item in point_list if int(item) > 0])

        return points

    @classmethod
    def rider_name(self, rider):
        name = rider[:1]

        return name

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


def configurate_heap(sourse_rider):
    rider_heap = []

    for index, rider in enumerate(sourse_rider):
        single_rider = RiderInfo(rider, index)
        heapq.heappush(rider_heap, single_rider)

    return rider_heap


if __name__ == "__main__":
    sourse_rider = []
    n = int(input())

    for _ in range(n):
        rider = list(map(str, input().split()))
        sourse_rider.append(rider)

    rider_heap = configurate_heap(sourse_rider)

    for driver in heapq.nlargest(n, rider_heap):
        print(driver)
