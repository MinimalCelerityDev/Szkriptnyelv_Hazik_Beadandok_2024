# verem.py

class Verem:
    def __init__(self) -> None:
        self.stack = []

    def __str__(self) -> str:
        return "[" + " ".join(map(str, self.stack))

    def ures(self) -> bool:
        return len(self.stack) == 0

    def betesz(self, elem: int) -> None:
        self.stack.append(elem)

    def kivesz(self) -> int | None:
        return self.stack.pop() if not self.ures() else None

    def meret(self) -> int:
        return len(self.stack)
