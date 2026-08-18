class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, res = prices[0], 0

        for p in prices[1:]:
            res = max(res, p - min_buy)
            min_buy = min(min_buy, p)
        
        return res