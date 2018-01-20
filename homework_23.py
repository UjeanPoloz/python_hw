import random

def is_repeat():
    choose = input('\nСыграем еще раз? Y or N: ')
    if choose == 'y' or choose == 'Y':
        return True
    elif choose == 'n' or choose == 'N':
        return False
    else:
        print('Введите Y - если хотите использовать дефолтный рейнд иди N - если нет')


while True:
    random_var = random.randint(0, 10)
    print('Попробуй угадать!')

    while True:
        user_number = int(input('Введите свое число: '))
        if user_number == random_var:
            print('\nПОЗДРАВЛЯЕМ! Вы угадали!! Загаданное число = %d' % random_var)
            break
        elif user_number < random_var:
            print('Мое значение больше')
        else:
            print('Мое значение меньше')

    if is_repeat() == False:
        break
