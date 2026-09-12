class Solution:
    def isValid(self, s: str) -> bool:
        peer = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in peer:
                stack.append(peer[c])
            elif not stack or c != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack