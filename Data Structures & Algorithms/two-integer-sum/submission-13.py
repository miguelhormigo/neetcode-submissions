class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d:
                return [d[rem], i]
            d[nums[i]] = i