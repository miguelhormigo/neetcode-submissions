class Solution:
    def isValid(self, s: str) -> bool:
        peer = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c not in peer.keys():
                if not stack or stack.pop() != c:
                    return False
            else:
                stack.append(peer[c])

        return not stack