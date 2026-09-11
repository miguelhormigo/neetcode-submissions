class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = 0
        l, r = 0, len(heights) - 1

        while l < r:
            hl, hr = heights[l], heights[r]
            sol = max(sol, min(hl, hr) * (r - l))
            if hl <= hr:
                l += 1
            else:
                r -= 1
        
        return sol