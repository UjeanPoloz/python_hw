catheter_a = int(input('Введите длину катета А:\n'))
catheter_b = int(input('Введите длину катета B:\n'))


def triangle_square_and_perimeter(a, b):
    square = 1/2 * a * b
    c = (a**2 + b**2)**0.5
    perimeter = a + b + c
    return square, perimeter

def print_answer(number):
    if number - int(number) == 0:
        print('Площадь треугольника равна: %d' % number)
    else:
        print('Площадь треугольника равна: %.3f' % number)

answer_square, answer_perimeter = triangle_square_and_perimeter(catheter_a, catheter_b)



print('-'*40)
print_answer(answer_square)
print_answer(answer_perimeter)
