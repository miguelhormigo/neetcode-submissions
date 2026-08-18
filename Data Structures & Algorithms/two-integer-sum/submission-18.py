from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter(nums)

        for i, n in enumerate(nums):
            peer = target - n
            if peer in c and (peer != n or c[peer] > 1):
                for j, m in enumerate(nums):
                    if j != i and m == peer:
                        return [i, j]