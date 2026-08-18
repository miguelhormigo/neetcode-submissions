from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            ndd = target - n
            if ndd in d:
                return [d[ndd], i]
            d[n] = i