class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        sol = 0

        while l <= r:
            m = (l + r) // 2
            print(m)

            if nums[l] >= nums[r]:
                if r == l + 1 and nums[l] > nums[r]:
                    return nums[r]
                if nums[m] <= nums[r]:
                    sol = m
                    if l < m and nums[m-1] > nums[m]:
                        break
                    r = m - 1
                elif nums[m] >= nums[l]:
                    l = m + 1
            else:
                sol = l
                r = m - 1
        
        return nums[sol]