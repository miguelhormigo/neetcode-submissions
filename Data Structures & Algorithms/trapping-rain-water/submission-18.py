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
                if height ==[4,2,0,3,2,5]:
                    print('>>>', result)
                l += 1
            else:
                result += min(lh, rh) - height[r]
                if height ==[4,2,0,3,2,5]:
                    print('<<<', result)
                r -= 1

        return result