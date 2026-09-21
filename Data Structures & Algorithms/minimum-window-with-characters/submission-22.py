class Solution:
    def minWindow(self, s: str, t: str) -> str:
        soll, solr, sol_len = 0, 0, len(s)+1
        l = 0

        tchars = set()
        count = defaultdict(int)
        for c in t:
            tchars.add(c)
            count[c] -= 1
        missing = len(count.keys())

        for r, c in enumerate(s):
            count[c] += 1
            if c in tchars and count[c] == 0:
                missing -= 1
            
            while missing == 0:
                if r - l < sol_len:
                    soll, solr, sol_len = l, r, r - l
                
                count[s[l]] -= 1
                if s[l] in tchars and count[s[l]] == -1:
                    missing += 1
                l += 1
        
        if sol_len <= len(s):
            return s[soll:solr+1]
        return ""