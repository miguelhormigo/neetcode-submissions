from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for c in s1:
            count[c] -= 1
        
        l = 0
        for r, c in enumerate(s2):
            count[c] += 1
            
            if count[c] == 0:
                del count[c]
            
            if (r - l) >= len(s1):
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
            
            if len(count.keys()) == 0:
                break
        
        return len(count.keys()) == 0