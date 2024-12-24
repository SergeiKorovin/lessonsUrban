from math import pi, sqrt, pow


class Figure:
    sides_count = 0
    filed = True

    def __init__(self,color:tuple, *sides):
        if len(sides) != self.sides_count and len(sides) != 1:
            self.__sides = [1 for _ in range(self.sides_count)]
        elif len(sides) == 1:
            self.__sides = [sides[0] for _ in range(self.sides_count)]
        self.__color = color

    def get_color(self):
        return list(self.__color)

    def get_sides(self):
        return list(self.__sides)

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and r in range(0, 256) and isinstance(g, int) and g in range(0, 256)\
                and isinstance(b, int) and b in range(0, 256):
            new_color = [r, g, b]
            self.__color = new_color
        return self.__color

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)

    def __is_valid_sides(self, args):
        if len(args) == self.sides_count:
            for i_args in args:
                if isinstance(i_args, int) and i_args >= 0:
                    return True
        else:
            return False

    def __len__(self):
        perimetr = 0
        for i in self.get_sides():
            perimetr += i
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        super().__len__()
        self.__radius = self.__len__() / (2 * pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return self.__len__() ** 2 / (4 * pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        super().__len__()

    def get_square(self):
        return sqrt((self.__len__() / 2) * ((self.__len__() / 2) - self.get_sides()[0]) *
                    ((self.__len__() / 2) - self.get_sides()[1]) * ((self.__len__() / 2) - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        return pow(self.get_sides()[0], 3)


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())