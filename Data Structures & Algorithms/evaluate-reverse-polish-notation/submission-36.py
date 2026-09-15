class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if t in ops:
                if t == '+':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                elif t == '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif t == '*':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                else:
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        
        return stack[-1]