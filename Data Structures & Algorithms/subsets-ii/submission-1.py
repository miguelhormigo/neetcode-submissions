from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = list(set(nums))
        sol = []

        def backtrack(i, subset):
            if i == len(nums):
                sol.append(subset.copy())
                return
            
            backtrack(i + 1, subset)

            n = nums[i]
            for c in range(counter[n]):
                subset.append(n)
                backtrack(i + 1, subset)
            # del subset[:-counter[n]]
            for c in range(counter[n]):
                subset.pop()
        
        backtrack(0, [])
        return sol