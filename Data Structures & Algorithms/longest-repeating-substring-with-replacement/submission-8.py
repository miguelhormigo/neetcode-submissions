from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 1
        count = Counter(s[0])
        l = 0
        maxc = s[0]
        maxcc = 1

        for r in range(1, len(s)):
            c = s[r]
            count[c] += 1
            if count[c] > maxcc:
                maxc, maxcc = c, count[c]
            
            while (r - l + 1) > (maxcc + k):
                c = s[l]
                count[c] -= 1
                l += 1
            
            maxl = max(maxl, r - l + 1)
        
        return maxl