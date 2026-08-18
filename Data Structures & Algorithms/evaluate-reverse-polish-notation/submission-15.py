class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        SIGNS = {'+', '-', '*', '/'}
        numbers = []

        for t in range(len(tokens)):
            t = tokens[t]
            if t not in SIGNS:
                numbers.append(int(t))
            else:
                n2 = numbers.pop()
                n1 = numbers.pop()
                if t == '+':
                    numbers.append(n1 + n2)
                elif t == '-':
                    numbers.append(n1 - n2)
                elif t == '*':
                    numbers.append(n1 * n2)
                else:
                    numbers.append(int(n1 / n2))

        return numbers.pop()