class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        return self.stack1.ures() and self.stack2.ures()

    def size(self):
        return self.stack1.meret()

    def append(self, value):
        self.stack1.betesz(value)

    def popleft(self):
        while not self.stack1.ures():
            self.stack2.betesz(self.stack1.kivesz())

        result = self.stack2.kivesz()

        while not self.stack2.ures():
            self.stack1.betesz(self.stack2.kivesz())

        return result

    def __str__(self):
        return "MyQueue(" + str(self.stack1.list) + ")"

class Stack:
    def __init__(self):
        self.list = []

    def ures(self):
        return not self.list

    def meret(self):
        return len(self.list)

    def betesz(self, value):
        self.list.append(value)

    def kivesz(self):
        if self.ures():
            return None

        return self.list.pop()

    def __str__(self):
        return "[" + " ".join([str(value) for value in self.list])


def main():
    sor = MyQueue()

    print("print(sor.is_empty()) -> ", end="")
    print(sor.is_empty())

    print("sor.append(1)\nsor.append(5)\nsor.append(6)")
    sor.append(1)
    sor.append(5)
    sor.append(6)

    print("print(sor) -> ", end="")
    print(sor)

    print("sor.popleft()")
    sor.popleft()

    print("print(sor) -> ", end="")
    print(sor)

    print("print(sor.size()) -> ", end="")
    print(sor.size())


if __name__ == "__main__":
    main()