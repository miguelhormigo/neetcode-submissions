class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = 0, len(height) - 1
        res = 0

        while l < r:
            if height[l] > height[r]:
                r -= 1

                if height[r] < height[maxr]:
                    res += min(height[maxl], height[maxr]) - height[r]
                else:
                    maxr = r
            else:
                l += 1

                if height[l] < height[maxl]:
                    res += min(height[maxl], height[maxr]) - height[l]
                else:
                    maxl = l
        
        return res