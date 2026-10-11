class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counter = defaultdict(int)
        for c in t:
            counter[c] -= 1
        missing = len(counter.keys())

        result_found, rl, rr = False, 0, len(s)
        l = 0
        for r, c in enumerate(s):
            if c in counter:
                counter[c] += 1
                if counter[c] == 0:
                    missing -= 1

            
            while missing == 0:
                if (r - l) < (rr - rl):
                    result_found = True
                    rl, rr = l, r
                
                if s[l] in counter:
                    counter[s[l]] -= 1
                    if counter[s[l]] == -1:
                        missing += 1
                l += 1
        
        if result_found:
            return s[rl:rr+1]
        return ""