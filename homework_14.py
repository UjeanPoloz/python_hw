def is_even(number):
    return number%2 == 0

def is_int(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


while True:

    while True:
        var = input('Введите целое число для проверки на четность:\n')
        if is_int(var):
            break
        else:
            print('Вы ввели не целое число')

    if is_even(int(var)):
        print('Число четное')
    else:
        print('Число нечетное')

    print(''*40)
