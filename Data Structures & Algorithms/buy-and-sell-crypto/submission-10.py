class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        buy = prices[0]

        for sell in prices[1:]:
            sol = max(sol, sell-buy)
            buy = min(buy, sell)
        
        return sol