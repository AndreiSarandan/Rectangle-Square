

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_height(self, new_height):
        self.height = new_height

    def set_width(self, new_width):
        self.width = new_width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        pic = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

    def get_amount_inside(self, x):
        return self.get_area() // x.get_area()

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, length):
        self.height = length
        self.width = length

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height

    def set_width(self, new_width):
        self.height = new_width
        self.width = new_width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def __repr__(self):
        return f'Square(side={self.height})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
sq.set_width(8)
print(sq)
