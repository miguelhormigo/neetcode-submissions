class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)
        mostfreq = s[0]
        l = 0

        for r, c in enumerate(s):
            count[c] += 1

            if count[c] >= count[mostfreq]:
                mostfreq = c

            while r - l + 1 - count[mostfreq] > k:
                count[s[l]] -= 1
                l += 1
                
                if count[c] >= count[mostfreq]:
                    mostfreq = c
            
            res = max(res, r - l + 1)
        
        return res