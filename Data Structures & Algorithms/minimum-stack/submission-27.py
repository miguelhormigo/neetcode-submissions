class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            v = val - self.min
            self.stack.append(v)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        v = self.stack.pop()
        if v < 0:
            new_min = self.min - v
            self.min = new_min

    def top(self) -> int:
        v = self.stack[-1]
        if v <= 0:
            return self.min
        else:
            return v + self.min

    def getMin(self) -> int:
        return self.min
