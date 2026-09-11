class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxl = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            seen.add(s[r])
            maxl = max(maxl, r-l+1)
        
        return maxl