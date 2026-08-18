class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, d2 = {}, {}
        for c in s1:
            d1[c] = d1.get(c, 0) + 1
        for c in s2[:len(s1)-1]:
            d2[c] = d2.get(c, 0) + 1

        l, r = 0, len(s1)-1
        while r < len(s2):
            c = s2[r]
            d2[c] = d2.get(c, 0) + 1

            if d1 == d2:
                return True
            
            c = s2[l]
            d2[c] -= 1
            if d2[c] == 0:
                del d2[c]

            l += 1
            r += 1

        return False