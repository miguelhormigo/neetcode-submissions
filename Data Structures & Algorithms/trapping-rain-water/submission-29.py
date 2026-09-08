class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ll = rl = 0
        sol = 0

        while l <= r:
            lh, rh = height[l], height[r]
            ll = max(ll, lh)
            rl = max(rl, rh)

            if ll < rl:
                sol += ll - lh
                l += 1
            else:
                sol += rl - rh
                r -= 1
        
        return sol