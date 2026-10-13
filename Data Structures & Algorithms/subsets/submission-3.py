class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        sub = []

        def dfs(i):
            nonlocal sub

            if i == len(nums):
                sol.append(sub.copy())
                return
            
            dfs(i + 1)
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
        
        dfs(0)
        return sol