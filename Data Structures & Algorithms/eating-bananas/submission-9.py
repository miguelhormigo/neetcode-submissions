import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = min(sum(piles) // h, 1), max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            if k == 0:
                break
            # print(l,r,k, end='->')

            total = 0
            for p in piles:
                total += math.ceil(p / k)
            # print(total)
            
            if total > h:
                l = k + 1
            elif total <= h:
                res = min(res, k)
                r = k - 1
        
        return res