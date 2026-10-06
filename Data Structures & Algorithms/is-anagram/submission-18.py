from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts, countt = Counter(s), Counter(t)
        return counts==countt