class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        r = 0

        for p in prices:
            if p < buy:
                buy = p
            else:
                r = max(r, p - buy)
        
        return r