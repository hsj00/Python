# wikidocs practice
# https://wikidocs.net/3465

# 6-1
## `point_x`와 `point_y`가 정의되지 않았다고 에러가 발생한다.
"""
class Point:
    def __init__(self, x, y):
        self.point_x = x
        self.point_y = y
        print("Coordinate of point is (%f, %f)." % (x, y))

    def setX(self, x):
        self.point_x = int(input("X: "))
        print("X is %f." % point_x)

    def setY(self, y):
        self.point_y = int(input("Y: "))
        print("Y is %f." % point_y)py

    def get(self):
        return (self.point_x, self.point_y)

    def move(self, dx, dy):
        self.point_x = x + dx
        self.point_y = y + dy
        print("Coordinate of point is (%f, %f)." % (self.point_x, self.point_y))


"""
# 6-1 solution
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
