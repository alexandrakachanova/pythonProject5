from point import Point2D
from manager1 import Manager

point1 = Point2D()
point2 = Point2D(3, 4)

print(point1)
print(point2)

man = Manager()
distance = man.calc_distance(point1, point2)

print(f"Distance between 2 points is {distance}.")