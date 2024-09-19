import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 2), round (circumference, 2)

area, circumference = circle_stats(5)

print("The area is: ", area, "and The circumference is: ", circumference)
