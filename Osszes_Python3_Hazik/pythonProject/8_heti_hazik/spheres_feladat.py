from math import *


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        if self.radius == other.radius:
            return "a két sugár egyenlő"

        if self.radius < other.radius:
            return "s sugara kisebb mint s2 sugara"
        else:
            return "s2 sugara kisebb mint s sugara"

    def __gt__(self, other):
        if self.radius == other.radius:
            return "a két sugár egyenlő"

        if self.radius > other.radius:
            return "s sugara nagyobb mint s2 sugara"
        else:
            return "s2 sugara nagyobb mint s sugara"

    def __ge__(self, other):
        if self.radius == other.radius:
            return "a két sugár egyenlő"

        if self.radius >= other.radius:
            return "s sugara nagyobb vagy egyenlő mint s2 sugara"
        else:
            return "s2 sugara nagyobb vagy egyenlő mint s sugara"

    def __le__(self, other):
        if self.radius == other.radius:
            return "a két sugár egyenlő"

        if self.radius <= other.radius:
            return "s sugara kisebb vagy egyenlő mint s2 sugara"
        else:
            return "s2 sugara kisebb vagy egyenlő mint s sugara"

    def surface(self):
        r = self.radius
        self.surface = 4 * pi * (r * r)
        return self.surface

    def volume(self):
        r = self.radius
        self.volume = (4 / 3) * pi * (r * r * r)
        return self.volume


class Ellipsoid:

    def volume(self, r1, r2, r3):
        self.volume = (4 / 3) * pi * (r1 * r2 * r3)
        return self.volume


def main():
    r = 2
    r2 = 3
    s = Sphere(r)
    s2 = Sphere(r2)

    print(s < s2)
    print(s > s2)
    print(s >= s2)
    print(s <= s2)

    print("Gömb térfogata: " + str(round(s.volume(), 2)))
    print("Gömb felszíne: " + str(round(s.surface(), 2)))

    e = Ellipsoid()
    r1 = float(2.4)
    r2 = float(1.5)
    r3 = float(3.4)
    print("Ellipszoid térfogata: " + str(round(e.volume(r1, r2, r3), 2)))


main()