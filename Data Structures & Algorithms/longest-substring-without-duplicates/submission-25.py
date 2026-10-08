class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = 0
        seen = {}
        l = r = 0 

        while r < len(s):
            c = s[r]
            if c in seen and l <= seen[c]:
                l = seen[c] + 1

            
            sol = max(sol, r - l + 1)

            seen[c] = r
            r += 1
        
        return sol