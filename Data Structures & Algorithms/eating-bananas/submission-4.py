import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            k = (l + r) // 2

            kh = 0
            for p in piles:
                kh += math.ceil(p / k)
            
            if kh <= h:
                r = k
            else:
                l = k + 1
        
        return l