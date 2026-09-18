class Solution:
    def trap(self, height: List[int]) -> int:
        sol = 0
        l, r = 0, len(height) - 1
        maxl = maxr = 0

        while l <= r:

            maxl = max(maxl, height[l])
            maxr = max(maxr, height[r])
            if maxl <= maxr:
                sol += maxl - height[l]
                l += 1
            else:
                sol += maxr - height[r]
                r -= 1
        
        return sol