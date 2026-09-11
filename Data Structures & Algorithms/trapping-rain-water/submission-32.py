class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        sol = 0

        while l < r:
            hl, hr = height[l], height[r]
            if hl <= hr:
                lmax = max(lmax, hl)
                sol += lmax - hl
                l += 1
            else:
                rmax = max(rmax, hr)
                sol += rmax - hr
                r -= 1
        
        return sol