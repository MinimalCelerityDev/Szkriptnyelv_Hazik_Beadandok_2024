class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __bool__(self):
        return self.area() == 0 or self.area() == 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return "Rectangle({w}, {h})".format(w=self.width, h=self.height)

def main():
    r1 = Rectangle(0, 5)
    r2 = Rectangle(10, 20)
    if r1:
        print("r1 hamisnak számít")
    else:
        print("r1 igaznak számít")
    print("-" * 20)
    print(r1 < r2)                     
    print(r2 < r1)

main()