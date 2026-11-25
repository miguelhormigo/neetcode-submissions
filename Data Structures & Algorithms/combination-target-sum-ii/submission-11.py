class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        counter = Counter(candidates)
        candidates = list(counter)

        def dfs(cur, cur_sum, i):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target or i == len(candidates):
                return
            
            new_sum = cur_sum
            for _ in range(counter[candidates[i]]):
                cur.append(candidates[i])
                new_sum += candidates[i]
                dfs(cur, new_sum, i + 1)
            for _ in range(counter[candidates[i]]):
                cur.pop()

            dfs(cur, cur_sum, i + 1)
        
        dfs([], 0, 0)
        return res