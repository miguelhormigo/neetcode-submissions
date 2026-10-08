class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = 0
        seen = {}
        l = 0

        for r in range(len(s)):
            c = s[r]
            if c in seen and l <= seen[c]:
                l = seen[c] + 1
            seen[c] = r
            
            sol = max(sol, r - l + 1)
        
        return sol