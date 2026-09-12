class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:        
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if not self.stack:
            self.min = None
        elif val < 0:
            self.min -= val

    def top(self) -> int:
        val = self.stack[-1]
        if val >= 0:
            return val + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
