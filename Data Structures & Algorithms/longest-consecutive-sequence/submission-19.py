class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        sol = 0

        for n in nums:
            if n not in seen:
                c = 1 + seen.get(n - 1, 0) + seen.get(n + 1, 0)
                seen[n] = c
                sol = max(sol, c)

                if n - 1 in seen:
                    seen[n - 1 - seen[n - 1] + 1] = c

                if n + 1 in seen:
                    seen[n + 1 + seen[n + 1] - 1] = c
        
        return sol