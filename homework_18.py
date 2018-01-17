while True:

    first_symbol = input('Введите 1ый символ unicode:\n')
    last_symbol = input('Введите последний символ unicode:\n')

    def sum_symbol_codes(first, last):

        first = ord(first)
        last = ord(last)

        sum = 0

        min_symbol = min(first, last)
        max_symbol = max(first, last)

        for i in range(min_symbol, max_symbol+1):
            sum = sum + i

        return sum

    print('\nСумма всех чисел в заданном промежутке равна: %d' % sum_symbol_codes(first_symbol, last_symbol))
    print(' \n')
