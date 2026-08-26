class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxl = 0
        start = 0

        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
                maxl = max(maxl, i-start+1)
            else:
                while start < i:
                    if s[start] == c:
                        start += 1
                        break
                    else:
                        seen.remove(s[start])
                    start += 1
        
        return maxl