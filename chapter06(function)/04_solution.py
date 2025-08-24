import math
def circle(rad):
    area = math.pi * (rad ** 2)
    circum = 2 * math.pi * rad
    return area, circum

area, circum = circle(3)
# print(circle(3.3))
print(area)
print(circum)