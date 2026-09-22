class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        p = self.stack.pop()
        if p < 0:
            v = self.min
            self.min = self.min - p
            return v
        return p + self.min

    def top(self) -> int:
        if not self.stack:
            return
        p = self.stack[-1]
        if p < 0:
            return self.min
        return p + self.min

    def getMin(self) -> int:
        return self.min