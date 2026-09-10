class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count = defaultdict(int)
        for c in s1:
            count[c] += 1

        l = 0
        for r in range(len(s2)):
            count[s2[r]] -= 1
            if count[s2[r]] == 0:
                del count[s2[r]]

            if r >= len(s1):
                count[s2[l]] += 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1


            if len(count.keys()) == 0:
                return True

        return False