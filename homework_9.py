def sep_print (symbol = '-', count = 60):
    print(symbol*count)

while True:

    while True:
        snake_style = input(str('Write stroke in snake_style: \n \r'))
        split_snake_style = snake_style.split('_')
        index = len(split_snake_style)

        if index == 1:
            sep_print('Wrong text style',1)
            sep_print()
        else:
            break

    ind = 0
    camelized_style = ''

    for ind in range(index):
        word = split_snake_style[ind]
        camelized_style = str(camelized_style + word.capitalize())

    sep_print('')
    print('Edited stroke in CamelizedStyle: %s' % camelized_style)
    sep_print()