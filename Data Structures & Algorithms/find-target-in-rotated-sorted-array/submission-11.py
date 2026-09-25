class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[l] <= nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[l] <= nums[m]:
                    if nums[m] < target:
                        l = m + 1
                    else:
                        if nums[l] <= target:
                            r = m - 1
                        else:
                            l = m + 1
                else:
                    if nums[m] < target:
                        if nums[r] >= target:
                            l = m + 1
                        else:
                            r = m - 1
                    else:
                        r = m - 1
        
        return -1