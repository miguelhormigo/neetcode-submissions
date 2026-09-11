class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        buy = prices[0]
        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                maxp = max(maxp, sell - buy)
        return maxp