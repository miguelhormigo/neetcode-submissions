class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d and d[rem] != i:
                return [i, d[rem]]