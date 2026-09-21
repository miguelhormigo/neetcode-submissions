class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for c in s1:
            count[c] -= 1
        
        rem = len(count.keys())

        l = 0
        for r, c in enumerate(s2):
            # print(l, r, s2[l:r+1], s2[l], end = ' -> ')

            count[c] += 1

            if count[c] == 0:
                del count[c]

            if r >= len(s1):
                count[s2[l]] -= 1

                if count[s2[l]] == 0:
                    del count[s2[l]]

                l += 1
            
            # print(count)
                
            if len(count.keys()) == 0:
                return True
            
        return False