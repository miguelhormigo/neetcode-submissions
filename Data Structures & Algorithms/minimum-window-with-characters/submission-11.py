from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        cs, ct = Counter(), Counter(t)

        l = bl = 0
        r, br = -1, len(s)

        while r < len(s):
            if missing > 0:
                r += 1
                if r == len(s):
                    break
                    
                c = s[r]
                if ct[c] > cs[c]:
                    missing -= 1
                cs[c] += 1
            else:
                if (r - l) < (br - bl):
                    bl, br = l, r
                c = s[l]
                if cs[c] > ct[c]:
                    cs[c] -= 1
                    l += 1
                elif r < len(s)-1:
                    r += 1
                    cs[s[r]] += 1
                else:
                    r += 1
        
        for c in ct:
            if ct[c] > cs[c]:
                return ""
        return s[bl:br+1]