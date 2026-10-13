class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol = []
        comb = []

        def dfs(left, i):
            nonlocal sol, comb

            if left == 0:
                sol.append(comb.copy())
                return
            if i == len(nums) or nums[i] > left:
                return
            
            dfs(left, i + 1)

            comb.append(nums[i])
            dfs(left - nums[i], i)
            comb.pop()
        
        dfs(target, 0)
        return sol

        # echar crema