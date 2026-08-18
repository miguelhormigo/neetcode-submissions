from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()

        maxl = l = r = 0
        while r < len(s):
            c[s[r]] += 1
            if c[s[r]] > 1:
                while l < r:
                    c[s[l]] -= 1
                    l += 1
                    if s[l-1] == s[r]:
                        break
            r += 1
            maxl = max(maxl, r-l)
        
        return maxl