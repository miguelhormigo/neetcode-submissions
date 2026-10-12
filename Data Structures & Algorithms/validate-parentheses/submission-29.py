class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'[': ']', '(': ')', '{': '}'}
        stack = []

        for c in s:
            if c in closing:
                stack.append(closing[c])
            else:
                if not stack or stack[-1] != c:
                    return False
                else:
                    stack.pop()
        
        return not stack