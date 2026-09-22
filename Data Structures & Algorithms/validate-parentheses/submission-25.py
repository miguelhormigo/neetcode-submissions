class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'[': ']', '{': '}', '(': ')'}
        stack = []

        for c in s:
            if c in closing:
                stack.append(closing[c])
            elif not stack or c != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack