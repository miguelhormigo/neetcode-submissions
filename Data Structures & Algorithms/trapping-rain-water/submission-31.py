class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ll = rl = 0
        sol = 0

        while l <= r:
            lh, rh = height[l], height[r]

            if ll < rl:
                ll = max(ll, lh)
                sol += ll - lh
                l += 1
            else:
                rl = max(rl, rh)
                sol += rl - rh
                r -= 1
        
        return sol