class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, res, seen, maxf = 0, 1, {s[0]: 1}, 1

        for i in range(1, len(s)):
            c = s[i]

            seen[c] = 1 + seen.get(c, 0)

            maxf = max(maxf, seen[c])

            while (i - start + 1 - maxf) > k:
                seen[s[start]] -= 1
                start += 1

            res = max(res, i - start + 1)
        
        return res