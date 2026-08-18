class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        peer = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in peer:
                if stack and stack[-1] == peer[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return stack == []