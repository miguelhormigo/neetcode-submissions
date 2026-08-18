class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                hl = height[l]
                left_max = max(left_max, hl)
                res += left_max - hl
            else:
                r -= 1
                hr = height[r]
                right_max = max(right_max, hr)
                res += right_max - hr
        
        return res