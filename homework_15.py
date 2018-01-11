var_x1 = 2
var_y1 = 2
radius_1 = 5

var_x2 = 9
var_y2 = 9
radius_2 = 8

def cirles_intersects(x1, y1, r1, x2, y2, r2):
    center_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    sum_radius = r1 + r2
    return center_distance <= sum_radius and center_distance >= abs(r1 - r2)

if cirles_intersects(var_x1,var_y1,radius_1,var_x2,var_y2,radius_2):
    print('Пересекаются')
else:
    print('Не пересекаются')

