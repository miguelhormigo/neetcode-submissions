import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        sol = max(piles)

        while l <= r:
            k = (l + r) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            
            if time > h:
                l = k + 1
            else:
                sol = min(sol, k)
                r = k - 1
        
        return sol