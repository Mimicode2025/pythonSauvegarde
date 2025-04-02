#question 3
from math import sin, pi

def degree_en_radians(degree):
    return degree * (pi / 180)

sinus_list = []
for angle in range(0, 91, 5):
    radians = degree_en_radians(angle)
    sinus_list.append(round(sin(radians), 3))

print(sinus_list)