class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height)-2
        lh, rh = height[0], height[-1]
        result = 0

        while l <= r:
            lh = max(lh, height[l])
            rh = max(rh, height[r])

            if lh <= rh:
                result += min(lh, rh) - height[l]
                l += 1
            else:
                result += min(lh, rh) - height[r]
                r -= 1

        return result