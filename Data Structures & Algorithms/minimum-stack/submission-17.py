class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        p = self.stack.pop()

        if p <= 0:
            ret = self.min
            self.min = self.min - p
            return ret
        else:
            return p + self.min

    def top(self) -> int:
        p = self.stack[-1]

        if p <= 0:
            ret = self.min
            return ret
        else:
            return p + self.min

    def getMin(self) -> int:
        return self.min
