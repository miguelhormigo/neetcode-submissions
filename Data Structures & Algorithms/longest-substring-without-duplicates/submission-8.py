class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = r = 0
        sol = 0

        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                sol = max(sol, r - l + 1)
                
            seen.add(s[r])
            
            r += 1
        
        return sol