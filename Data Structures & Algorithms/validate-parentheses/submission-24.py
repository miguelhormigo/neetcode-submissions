class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'{': '}', '(': ')', '[': ']'}
        stack = []

        for c in s:
            if c in closing:
                stack.append(closing[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        
        return not stack