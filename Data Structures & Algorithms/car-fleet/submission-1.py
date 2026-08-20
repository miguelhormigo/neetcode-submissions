import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = {}
        for i, p in enumerate(position):
            speeds[p] = speed[i]
        
        position.sort(reverse=True)
        stack = []
        for p in position:
            r = (target - p) / speeds[p]
            # print(p, stack, r)
            if not stack or stack[-1] < r:
                stack.append(r)
        
        print(stack)
        return len(stack)