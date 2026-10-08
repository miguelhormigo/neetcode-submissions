class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, res_s = [], set()

        cur, cur_sum = [], 0

        def backtrack(i):
            nonlocal cur, cur_sum

            if cur_sum == target:
                key = tuple(cur)
                res.append(cur.copy())
                res_s.add(key)
                return
            
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if cur_sum + candidates[j] > target:
                    return
                
                print(cur)
                
                cur.append(candidates[j])
                cur_sum += candidates[j]
                backtrack(j+1)
                cur.pop()
                cur_sum -= candidates[j]
        
        backtrack(0)
        return res