class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        counter = Counter(candidates)
        res, cur = [], []

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or candidates[i] + cur_sum > target:
                return
            
            print(candidates[i], cur_sum)

            backtrack(i + counter[candidates[i]], cur_sum)
            
            for c in range(1, counter[candidates[i]] + 1):
                cur.append(candidates[i])
                cur_sum += candidates[i]
                backtrack(i + counter[candidates[i]], cur_sum)
            
            for c in range(2, counter[candidates[i]] + 1):
                cur.pop()
                cur_sum -= candidates[i]

            cur.pop()

        backtrack(0, 0)
        return res