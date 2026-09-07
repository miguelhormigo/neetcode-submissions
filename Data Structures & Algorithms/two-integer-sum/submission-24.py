class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in pos:
                return [pos[n], i]
            pos[nums[i]] = i