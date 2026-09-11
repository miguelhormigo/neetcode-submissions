class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxl = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            maxl = max(maxl, r-l+1)
            seen[s[r]] = r
        
        return maxl