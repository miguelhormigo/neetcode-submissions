from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1, c2 = Counter(s1), Counter()
        l = 0
        for r in range(len(s2)):
            if s1 == 'adc':
                print(c1, c2)
            if r >= len(s1):
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1

            c2[s2[r]] += 1
            if c1 == c2:
                return True

        return False