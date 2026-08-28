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
                left = s2[l]
                count[left] -= 1
                if count[left] == 0:
                    del count[left]
                l += 1
            
            if len(count.keys()) == 0:
                break
        
        return len(count.keys()) == 0