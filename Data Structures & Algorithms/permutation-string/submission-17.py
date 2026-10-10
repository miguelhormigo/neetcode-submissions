class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for c in s1:
            counter[c] -= 1
        missing = len(counter.keys())
        l = 0

        for r, c in enumerate(s2):
            print(l,r, missing)
            counter[c] += 1
            if counter[c] == 0:
                missing -= 1
            elif counter[c] == 1:
                missing += 1

            if r >= len(s1):
                left = s2[l]
                counter[left] -= 1
                if counter[left] == 0:
                    missing -= 1
                elif counter[left] == -1:
                    missing += 1
                l += 1
            
            if missing == 0:
                return True
        
        return False