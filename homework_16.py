print('Между поездами 10км. На пути первого поезда через 4км. есть разъезд.')


speed_v1 = int(input('При скорости первого поезда равной:'))
speed_v2 = int(input('А скорость второго поезда:'))

def have_trains_crashed(v1, v2):
    total_distance = 10
    second_way = 4

    time_v1 = second_way / v1
    time_v2 = (total_distance - second_way) / v2

    return time_v2 <= time_v1


if have_trains_crashed(speed_v1,speed_v2):
    print('Поезда cтолкнутся')
else:
    print('Поезда не столкнутся')