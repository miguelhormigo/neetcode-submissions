class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in closing:
                stack.append(closing[c])
            else:
                if not stack or stack.pop() != c:
                    return False
        
        return not stack