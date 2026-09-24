import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, math.ceil((max(piles) * len(piles)) / h)
        sol = float('inf')

        while l <= r:
            k = (l + r) // 2
            
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            
            if total > h:
                l = k + 1
            else:
                sol = min(sol, k)
                r = k - 1
        
        return sol