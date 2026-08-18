class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        bestl, bestlh = 0, 0
        bestr, bestrh = len(heights)-1, 0

        most = 0
        while l < r:
            hl, hr = heights[l], heights[r]
            if (hl - l - bestl) > bestlh:
                bestl = l
                bestlh = hl
            if (hr - bestr - r) > bestrh:
                bestr = r
                bestrh = hr
            most = max(most, min(hl, hr) * (r - l))

            if hl < hr:
                l += 1
            else:
                r -= 1
        
        return most