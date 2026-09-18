class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        b = prices[0]
        for p in prices[1:]:
            sol = max(sol, p-b)
            b = min(b, p)
        return sol