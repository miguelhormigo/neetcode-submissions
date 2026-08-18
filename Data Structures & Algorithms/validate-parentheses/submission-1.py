class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        peer = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in peer:
                if not stack or stack[-1] != peer[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return stack == []