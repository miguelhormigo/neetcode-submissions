class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        sol = 0

        for r in range(len(s)):
            if seen.get(s[r], -1) >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            sol = max(sol, r - l + 1)
        
        return sol