class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        SIGNS = {'+', '-', '*', '/'}

        stack = []

        for c in tokens:

            if c in SIGNS:
                if c == '+':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                elif c == '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif c == '*':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                else:
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
            else:
                stack.append(int(c))
        
        return stack[-1]