from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = Counter(nums)

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in counter:
                for j in range(len(nums)):
                    if j != i and nums[j] == rem:
                        return [i, j]