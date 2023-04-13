class Circle:

    def __init__(self):
        self.radius = float(input("Please enter your desired radius of the circle: "))
        self.diameter = float(input("Please enter your desired diameter of the circle: "))

#let a be equal to area and let p be equal to perimeter

    def a(self):
        return 3.14159 * (self.radius ** 2)

    def p(self):
        return 2 * 3.14159 * self.radius

crcl = Circle()
print("The Area of the Circle =", crcl.a())
print("The Perimeter of the Circle =", crcl.p())