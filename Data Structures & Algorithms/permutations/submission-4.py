class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def dfs(perm, i):
            if i == len(nums):
                sol.append(perm.copy())
                return

            for j in range(i, len(nums)):
                perm[i], perm[j] = perm[j], perm[i]
                dfs(perm, i + 1)
                perm[i], perm[j] = perm[j], perm[i]
        
        dfs(nums, 0)
        return sol