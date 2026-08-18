class Solution:
    def is_num(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
        
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for t in range(len(tokens)):
            t = tokens[t]
            if self.is_num(t):
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