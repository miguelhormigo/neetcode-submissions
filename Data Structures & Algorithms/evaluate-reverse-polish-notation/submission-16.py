class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        SIGNS = {'+', '-', '*', '/'}
        numbers = []

        for t in range(len(tokens)):
            t = tokens[t]
            if t not in SIGNS:
                numbers.append(int(t))
            else:
                a, b = numbers.pop(), numbers.pop()
                if t == '+':
                    numbers.append(a + b)
                elif t == '-':
                    numbers.append(b - a)
                elif t == '*':
                    numbers.append(a * b)
                else:
                    numbers.append(int(b / a))

        return numbers.pop()