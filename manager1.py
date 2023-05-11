# дженити классы
# классы сущности
# функциональные классы (реализуется основная бизнес логика)

from point import Point2D
import math
class Manager:
    def calc_distance(self, point1, point2):
        if isinstance(point1, Point2D) and isinstance(point2, Point2D):
            dx = point1.get_x() - point2.get_x()
            dy = point1.get_y() - point2.get_y()
            distance = math.sqrt(dx ** 2 + dy ** 2)
            return distance
        return -1