class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res, seen = 0, 0, set()

        for i, c in enumerate(s):
            if c in seen:
                while s[start] != c:
                    seen.remove(s[start])
                    start += 1
                start += 1
            else:
                seen.add(c)
                res = max(res, i - start + 1)
        
        return res