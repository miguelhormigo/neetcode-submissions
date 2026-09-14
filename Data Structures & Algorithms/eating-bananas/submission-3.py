import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minr, maxr = 1, max(piles)
        l, r = minr, maxr

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