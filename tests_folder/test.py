class Square:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value



sq = Square(1, 2)
print(sq.x)

sq.x = 3
print(sq.x)
