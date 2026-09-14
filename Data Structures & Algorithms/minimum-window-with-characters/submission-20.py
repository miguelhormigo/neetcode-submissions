class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = {}
        need = 0
        for c in t:
            if c not in count:
                count[c] = -1
                need += 1
            else:
                count[c] -= 1
        
        sol, sl, sr = float('inf'), 0, -1
        have = 0
        l = 0
        for r, c in enumerate(s):
            if c in count:
                if count[c] == -1:
                    have += 1

                count[c] += 1

                while have == need:
                    # print(l,r,need,have)
                    if (r - l + 1) < sol:
                        sol, sl, sr = r - l + 1, l, r

                    if s[l] in count:
                        if count[s[l]] == 0:
                            have -= 1
                        count[s[l]] -= 1
                    l += 1
        
        return s[sl:sr+1]