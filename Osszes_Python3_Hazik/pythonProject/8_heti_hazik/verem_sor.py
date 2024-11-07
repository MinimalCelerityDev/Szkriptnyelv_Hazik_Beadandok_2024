class Verem:
    verem = []

    def ures(self):
        if len(self.verem) == 0:
            return "True"
        else:
            return "False"

    def betesz(self, num):
        self.verem.append(num)

    def kivesz(self):
        if len(self.verem) > 0:
            self.verem.pop()
        else:
            return "None"

    def meret(self):
        return len(self.verem)

    def __str__(self):
        return str(self.verem)


class Sor:
    sor = []

    def ures(self):
        if len(self.sor) == 0:
            return "True"
        else:
            return "False"

    def betesz(self, num):
        self.sor.append(num)

    def kivesz(self):
        if len(self.sor) > 0:
            self.sor.pop(0)
        else:
            return "None"

    def meret(self):
        return len(self.sor)

    def __str__(self):
        return str(self.sor)


def main():
    # verem

    v = Verem()
    print(v)  
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)

    print("-" * 20)

    v = Sor()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


main()