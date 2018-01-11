print('Решение квдартного уровня ax^2+bx+c=0')

while True:
    var_a = int(input('Введите значение для переменной а:'))
    if var_a == 0:
        print('a должно быть отличным от 0')
    else:
        break

var_b = int(input('Введите значение для переменной b:'))
var_c = int(input('Введите значение для переменной c:'))


def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
    d = b**2 - 4 * a * c
    if d < 0:
        return None, None
    elif d == 0:
        x = -b / (2 * a)
        return x, None
    else:
        x_1 = (-b + d**0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return x_1, x_2

print(solve_quadratic_equation(var_a, var_b, var_c))




