class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            need = target - n
            if need in seen:
                return [seen[need], i + 1]
            seen[n] = i + 1