class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        missing = k
        most_freq = s[0]
        max_l = 0
        l = r = 0

        while r < len(s):
            count[s[r]] += 1
            if s[r] != most_freq:
                missing -= 1
                while missing < 0:
                    if count[s[r]] >= count[most_freq]:
                        missing = missing + count[s[r]] - count[most_freq]
                        most_freq = s[r]
                        if missing >= 0:
                            break
                    if s[l] != most_freq:
                        missing += 1
                    count[s[l]] -= 1
                    l += 1
            max_l = max(max_l, r - l + 1)
            r += 1
        
        return max_l