'''
Help Alla to write the code of the algorithm to select the classes that will
take place in the classroom.
Given is the subject schedule. You need to build a schedule according to which
you can have as many classes in the classroom as possible.

Input format
The first line contains the number of subjects. Then, for each subject, a
separate line records the start and end time of the lesson.

Output format
Print all classes to be taken in the classroom, in order of increasing
start time.
Notes
If there are several optimal options, you should choose the lesson that
started earlier.
It is possible to spend more than one lesson of zero duration at once.
'''

from decimal import Decimal


def find_earliest_class(class_list):
    end_time = 0
    schedule_list = []
    for lesson in class_list:
        if end_time <= lesson[0]:
            end_time = lesson[1]
            schedule_list.append(lesson)
    return schedule_list


def main():
    amount = int(input())
    count = 1
    new_list = []
    for i in range(amount):
        new_list.append(0)
        new_list[i] = []

    while count <= amount:
        for k in range(amount):
            new_list[k] = list(map(str, input().split()))
            j = 0
            for number in new_list[k]:
                while j <= 1:
                    try:
                        new_list[k][j] = int(number)
                    except ValueError:
                        new_list[k][j] = Decimal(number).normalize()
                    j += 1
                    break
            count += 1

    new_list = sorted(new_list, key=lambda x: (x[1], x[0]))
    schedule_list = find_earliest_class(new_list)
    print(len(schedule_list))
    for item in schedule_list:
        print(*item)


if __name__ == '__main__':
    main()
