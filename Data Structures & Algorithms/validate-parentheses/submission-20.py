class Solution:
    def isValid(self, s: str) -> bool:
        peer = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in peer:
                stack.append(peer[c])
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack