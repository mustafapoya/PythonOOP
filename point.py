import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft.x < self.x < upright.x and lowleft.y < self.y < upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, lowleft: Point, upright: Point):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)



point1 = Point(7, 8)
print(point1.x, point1.y)


print("john".count("j"))
print("john".capitalize())

# print(Point(3, 4).falls_in_rectangle((1, 1), (6, 6)))

point1 = Point(1, 1)
point2 = Point(2, 2)
print(point1.distance_from_point(point2))

#
rectanglex = Rectangle(point1, point2)

from random import randint

rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))

print("Rectangle Coordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and", rectangle.upright.x, ",", rectangle.upright.y)

user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

user_area = float(input("Guess rectangle area: "))

print("your area was off by: ", rectangle.area() - user_area)

print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle.lowleft, rectangle.upright))