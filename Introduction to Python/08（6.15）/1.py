from math import sqrt


class Reg_polygon(object):
    def __init__(self, edges, length):
        self.edges = edges
        self.length = length

    def perimeter(self):
        return self.edges * self.length


class Triangle(Reg_polygon):
    def __init__(self, length):
        super().__init__(3, length)

    def area(self):
        return sqrt(3) / 2 * self.length * self.length / 2

    def __str__(self):
        return "Triangle"


class Square(Reg_polygon):
    def __init__(self, length):
        super().__init__(4, length)

    def area(self):
        return self.length * self.length

    def __str__(self):
        return "Square"


triangle = Triangle(10)
square = Square(10)
for shape in [triangle, square]:
    print(f"{shape}\n周囲の長さ：{shape.perimeter():d}\n面積{shape.area():.2f}")