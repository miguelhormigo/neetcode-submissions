from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()

        maxl = l = r = 0
        while r < len(s):
            c = s[r]
            count[c] += 1
            if count[c] > 1:
                while l < r:
                    count[s[l]] -= 1
                    l += 1
                    if s[l-1] == c:
                        break
            r += 1
            maxl = max(maxl, r-l)
        
        return maxl