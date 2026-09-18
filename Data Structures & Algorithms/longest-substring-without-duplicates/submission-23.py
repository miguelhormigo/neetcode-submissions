class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sol = 0
        seen = {}

        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            seen[c] = r

            sol = max(sol, r - l + 1)

        return sol