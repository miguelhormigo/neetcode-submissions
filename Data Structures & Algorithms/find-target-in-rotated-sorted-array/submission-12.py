class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    if nums[m] < target or nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1
                elif nums[m] <= nums[r]:
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                break
        
        return -1