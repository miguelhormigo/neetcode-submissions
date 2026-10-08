class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            m = target-n
            if m in seen:
                return [seen[m]+1, i+1]
            seen[n] = i