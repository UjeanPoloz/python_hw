import random

def fill_list_by_randoms(num_limit, ind, lower_bound = -100, upper_bound = 100):
    for i in range(ind):
        num_limit.append(random.randint(lower_bound, upper_bound))

def diff_min_max(num_limit):
    num_limit.sort()

    if num_limit[0] < 0:
        res = num_limit[len(num_limit) - 1] + num_limit[0]
    else:
        res = num_limit[len(num_limit) - 1] - num_limit[0]

    return res

num_limit = []
ind = int(input('Введите длину числового диапозана:'))

while True:
    choose = input('\nИспользовать дефолтный рейндж от -100 до 100? Y or N: \n')

    if choose == 'y' or choose == 'Y':
        lower_bound = -100
        upper_bound = 100
        fill_list_by_randoms(num_limit, ind)
        break
    elif choose == 'n' or choose == 'N':
        lower_bound = int(input('\nВведите нижнее значение диапозана:\t'))
        upper_bound = int(input('\nВведите верхнее значение диапозана:\t'))
        fill_list_by_randoms(num_limit, ind, lower_bound, upper_bound)
        break
    else:
        print('Введите Y - если хотите использовать дефолтный рейнд иди N - если нет')


print('\nСпсиок:', num_limit)

print('Разница между минимальным и максимальным значением равна:%d' % diff_min_max(num_limit))