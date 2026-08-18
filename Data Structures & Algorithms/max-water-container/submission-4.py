class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        most = 0
        while l < r:
            hl, hr = heights[l], heights[r]
            most = max(most, min(hl, hr) * (r - l))

            if hl < hr:
                l += 1
            else:
                r -= 1
        
        return most