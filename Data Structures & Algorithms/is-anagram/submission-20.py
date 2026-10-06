class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        for c in t:
            counts[c] -= 1
            if counts[c] == 0:
                del counts[c]

        return len(counts) == 0