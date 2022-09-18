from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        # go to a certain coordinate
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        turtle.done()


gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))
myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)



# rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
#
# print("Rectangle Coordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and", rectangle.upright.x, ",", rectangle.upright.y)
#
# user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
#
# user_area = float(input("Guess rectangle area: "))
#
# print("your area was off by: ", rectangle.area() - user_area)
#
# print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))