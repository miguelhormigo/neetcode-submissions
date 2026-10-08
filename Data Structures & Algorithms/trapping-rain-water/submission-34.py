class Solution:
    def trap(self, height: List[int]) -> int:
        sol = 0
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]

        while l < r:
            if maxl <= maxr:
                sol += maxl - height[l]
                l += 1
                maxl = max(maxl, height[l])
            else:
                sol += maxr - height[r]
                r -= 1
                maxr = max(maxr, height[r])
        
        return sol