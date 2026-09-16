class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                if (nums[m] < nums[r] and target <= nums[r]) or nums[m] >= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > target:
                if (nums[m] > nums[l] and target >= nums[l]) or nums[m] < nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                return m
        
        return -1