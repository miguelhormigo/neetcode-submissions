class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxl = 0
        l = 0

        for r in range(len(s)):
            if seen.get(s[r], -1) >= l:
                l = seen[s[r]] + 1
            maxl = max(maxl, r-l+1)
            seen[s[r]] = r
        
        return maxl