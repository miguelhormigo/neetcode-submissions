class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            hl, hr = heights[l], heights[r]
            res = max(res, min(hl, hr) * (r - l))

            if hl > hr:
                r -= 1
            else:
                l += 1

        return res