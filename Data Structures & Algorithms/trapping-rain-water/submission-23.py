class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lh, rh = height[l], height[r]
        result = 0

        while l < r:
            if lh <= rh:
                l += 1
                lh = max(lh, height[l])
                result += lh - height[l]
            else:
                r -= 1
                rh = max(rh, height[r])
                result += rh - height[r]

        return result