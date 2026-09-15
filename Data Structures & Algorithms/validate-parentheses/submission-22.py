class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'{': '}', '(': ')', '[': ']'}
        stack = []

        for c in s:
            print(c, stack, c in closing, not stack or stack[-1] != c)
            if c in closing:
                stack.append(closing[c])
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()
        
        return not stack