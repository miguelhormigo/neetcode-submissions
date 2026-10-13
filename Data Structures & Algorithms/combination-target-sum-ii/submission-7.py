class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        comb = []
        print(candidates)

        def dfs(i, cur_sum):
            if cur_sum == target:
                sol.append(comb.copy())
                return
            if cur_sum > target or i == len(candidates):
                return
            
            dfs(i + 1, cur_sum)
            
            if i == 0 or candidates[i-1] != candidates[i]:
                rep = 1
                for j in range(i + 1, len(candidates)):
                    if candidates[j] == candidates[i]:
                        rep += 1
                
                for r in range(1, rep + 1):
                    comb.append(candidates[i])
                    dfs(i + 1, cur_sum + candidates[i] * r)
                del comb[-r:]

        dfs(0, 0)
        return sol