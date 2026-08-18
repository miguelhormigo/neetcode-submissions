class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        biggest = 0

        while l < r:
            cur = min(heights[l], heights[r]) * (r-l)
            if cur > biggest:
                biggest = cur
                print(l,r)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return biggest