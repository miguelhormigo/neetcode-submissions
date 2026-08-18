class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()

        maxl = l = r = 0
        while r < len(s):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            r += 1
            maxl = max(maxl, r-l)
        
        return maxl