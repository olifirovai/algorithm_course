'''
The IT conference was attended by students from different universities from
all over the country. The list of students is presented in the table.
The column " University" contains the numbers - id of the university.
Joan offers Tom to find out from which universities at the conference came the
most students. The guys decided to find out from which k universities there
are the most guests.
The first line gives the list of the id of universities.
The second line gives one number - parameter k.
'''


def top_university(students_list, amount):
    student_dict = {c: students_list.count(c) for c in set(students_list)}
    sorted_dict = {k: student_dict[k] for k in
                   sorted(student_dict, key=student_dict.get, reverse=True)}
    top_university = list(sorted_dict.keys())[:amount]
    print(*top_university)


students_list = list(map(int, input().split()))
amount = int(input())

top_university(students_list, amount)
