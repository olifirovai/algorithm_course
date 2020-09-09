'''

'''


# номер успешной посылки: 34247255

# комментарии от Никиты Ковалева к этому коду:

# какой-то очень хитрый алгоритм, вот эти махинации с общей суммой и делением
# не тянут на настоящую жадность.
# Если не получится настоящей жадностью, то я хотел бы увидеть комментом
# алгоритм, который здесь применяется, ибо пока я понять его не могу


# Я бы очень хотела разобраться почему это алгоритм не является жадным.
# Поэтому, я постаралась написать комментарии по его реализации.
# Этот способ мне напоминает переливание воды из стакана в стакан, для
# выравнивания уровней, но только в ситуации со стаканами мы добавляем воду,
# в нашем случае с фотографиями Отнимаем.


def max_photo(capacity_list):
    max_photos = 0
    for number in capacity_list:
        max_photos += number
    return max_photos


def data_center(n, capacity_list, max_photos):
    if n < 2:
        print(0)

    elif len(capacity_list) == 2:
        max_number = max(capacity_list[0], capacity_list[1])
        min_number = min(capacity_list[0], capacity_list[1])
        lost_number = max_number - min_number
        max_photos = (max_photos - lost_number) // 2
        print(max_photos)

    else:
        '''
        Этот алгоритм позволяет распределить меньший элемент между бОльшими 
        двумя так, чтобы эти бОльшие два элемента максимально выровнятся между
        собой. Он уменьшает самый большой элемент пока тот не сравняется со 
        вторым элементом. Дальше он уменьшает бОльшие два элемента в равной 
        степени. Тем самым они равномерно уменьшаются. Если же величины 
        меньшего элемента не хватает чтобы выровнять бОльшие два элемента 
        между собой, меньший элемент просто уменьшает самый большой 
        элемент.
        '''
        capacity_list.sort()
        min_number = capacity_list[0]
        max_number = capacity_list[-1]
        prev_max_number = capacity_list[-2]
        operate_number = max_number - prev_max_number
        max_number -= min(min_number, operate_number)
        min_number = max(0, capacity_list[0] - operate_number)
        prev_max_number -= min_number // 2
        max_number -= min_number // 2
        min_number %= 2
        max_number -= min_number
        min_number = 0
        capacity_list[-2] = prev_max_number
        capacity_list[-1] = max_number
        capacity_list[0] = min_number
        capacity_list.pop(min_number)
        data_center(n, capacity_list, max_photos)


n = int(input())
capacity_list = list(map(int, input().split()))

max_photos = max_photo(capacity_list)
data_center(n, capacity_list, max_photos)
