'''



'''


class Schedule:
    def __init__(self, time_list):
        self.classes = []
        self.start_time = time_list[0]
        self.end_time = time_list[1]

    def add_class(self):
        self.classes.append([self.start_time, self.end_time])

    def find_earliest_class(self):
        earliest_class = []
        while True:
            for i in range(len(self.classes)):
                early_class = []
                if self.classes[i][1] == self.classes[i][0]:
                    schedule_list.append(self.classes[i])
                if i == 0:
                    early_class = self.classes[i]
                if early_class[1] < self.classes[i][1]:
                    early_class = self.classes[i]
                elif early_class[1] == self.classes[i][1]:
                    early_class = min(early_class[0], self.classes[i][1])

    def make_schedule(self):

        pass


schedule_list = []


def main():
    amount = int(input())
    for obj in range(amount):
        data = list(map(float, input().split()))
        obj = Schedule(data)
        obj.add_class()


if __name__ == '__main__':
    main()
