while True:

    first_symbol = input('Введите 1ый символ unicode:\n')
    last_symbol = input('Введите последний символ unicode:\n')

    def sum_symbol_codes(first, last):
        first = ord(first)
        last = ord(last)
        sum = 0
        if first < last:
            ind = last - first + 1
            for i in range(ind):
                sum = sum + first
                first = first + 1
        elif first == last:
            sum = first
        else:
            ind = first - last + 1
            for i in range(ind):
                sum = sum + last
                last = last + 1
        return sum

    print('\nСумма всех чисел в заданном промежутке равна: %d' % sum_symbol_codes(first_symbol, last_symbol))
    print(' \n')