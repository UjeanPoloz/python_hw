import random

def get_max_digit(number):
    get_len = len(str(number))
    max_digit = 0

    for i in range(get_len):
        digit = number - (int(number / 10) * 10)
        number = int(number / 10)

        if digit > max_digit:
            max_digit = digit

    return max_digit

while True:
    choose = input('Хотите использовать случайное 12ти-значное число? Y or N: \n')

    if choose == 'y' or choose == 'Y':
        number = random.randint(100000000000, 999999999999)
        print('Случайное число: %d' % number)
        break
    elif choose == 'n' or choose == 'N':
        number = int(input('\nВведите любое свое число: '))
        break
    else:
        print('Введите Y - если хотите использовать дефолтный рейнд иди N - если нет')



print('Наибольшая цифра числа: %d' % get_max_digit(number))
