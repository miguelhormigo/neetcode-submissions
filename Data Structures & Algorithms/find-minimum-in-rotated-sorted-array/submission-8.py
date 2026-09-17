class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # print(l,r,m,nums[m],res)

            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            else:
                if nums[m] >= nums[l]:
                    # go right
                    l = m + 1
                elif nums[m] < nums[l]:
                    # save numsm and go left
                    res = min(res, nums[m])
                    r = m - 1
        
        return res