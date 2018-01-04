import math

def degrees2radians(degrees):
    radian = (degrees * math.pi) / 180
    return float(radian)

print('Значение cos(60°) равно: %f\n'
      'Значение cos(45°) равно: %f\n'
      'Значение cos(40°) равно: %f\n'% (math.cos(degrees2radians(60)),
                                         math.cos(degrees2radians(45)),
                                         math.cos(degrees2radians(40))))





