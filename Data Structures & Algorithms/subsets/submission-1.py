class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = set()

        def backtrack(current, i):
            key = tuple(current)
            if key in sols:
                return
            
            sols.add(key)

            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                current.append(nums[j])
                backtrack(current, j + 1)
                current.pop()
        
        backtrack([], 0)

        return [list(sol) for sol in sols]