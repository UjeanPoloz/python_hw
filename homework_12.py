number = int(input('Введите трех значение число:\n'))

def sum_of_digits(number):
    number = int(number)
    hundreds = int(number / 100)
    tens = int((number - hundreds * 100) / 10)
    numbers = int((number - hundreds * 100 - tens * 10))
    sum = hundreds + tens + numbers
    return int(sum)

def sum_of_digits_str(number):
    number_str = str(number)
    sum_str = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
    return int(sum_str)

print(' '*50)
print('РЕШЕНИЕ C ИСПОЛЬЗОВАНИЕМ СТРОК:')
print('Сумма всех чисел введенного числа равна: %d' % sum_of_digits_str(number))


print('-'*50)
print('РЕШЕНИЕ БЕЗ ИСПОЛЬЗОВАНИЯ СТРОК:')
print('Сумма всех чисел введенного числа равна: %d' % sum_of_digits(number))
