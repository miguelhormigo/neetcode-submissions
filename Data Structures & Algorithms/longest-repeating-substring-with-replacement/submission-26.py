class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_l = 0
        mf = 0
        l = 0

        for r, c in enumerate(s):
            count[c] += 1
            
            if count[c] >= mf:
                mf = count[c]

            while (r - l + 1 - mf) > k:
                count[s[l]] -= 1
                l += 1

                if count[c] >= mf:
                    mf = count[c]
            
            max_l = max(max_l, (r - l + 1))
        
        return max_l