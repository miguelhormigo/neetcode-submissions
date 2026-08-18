class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        buyp = prices[0]

        for p in prices:
            if p < buyp:
                buyp = p
            else:
                r = max(r, p - buyp)
        
        return r