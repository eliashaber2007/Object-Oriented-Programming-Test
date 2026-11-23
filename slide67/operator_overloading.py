import math


# Problem 1
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


# Problem 2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age


# Problem 4
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        # dot product
        return self.x * other.x + self.y * other.y + self.z * other.z


# Problem 5
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius


# Problem 6
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()


# Problem 7
class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __mul__(self, other):
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Columns of the first matrix must equal rows of the second")
        result = []
        for i in range(len(self.rows)):
            new_row = []
            for j in range(len(other.rows[0])):
                total = 0
                for k in range(len(other.rows)):
                    total += self.rows[i][k] * other.rows[k][j]
                new_row.append(total)
            result.append(new_row)
        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)


if __name__ == "__main__":
    c1 = ComplexNumber(3, 2)
    c2 = ComplexNumber(1, 5)
    print("Complex add:", c1 + c2)
    print("Complex sub:", c1 - c2)

    p1 = Person("Elias", 18, "M")
    p2 = Person("Sara", 21, "F")
    print("p1 > p2:", p1 > p2)

    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print("Dot product:", v1 * v2)

    small, big = Circle(2), Circle(5)
    print("small < big:", small < big, "| small == big:", small == big, "| big >= small:", big >= small)

    a, b = Point(3, 4), Point(1, 1)
    print("a > b:", a > b, "| a == Point(4, 3):", a == Point(4, 3))

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("Matrix product:")
    print(m1 * m2)
