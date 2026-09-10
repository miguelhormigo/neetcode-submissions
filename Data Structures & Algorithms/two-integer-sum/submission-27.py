class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        avail = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in avail:
                return [avail[diff], i]
            avail[n] = i