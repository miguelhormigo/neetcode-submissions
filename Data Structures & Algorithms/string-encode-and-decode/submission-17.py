class Solution:

    def encode(self, strs: List[str]) -> str:
        r = []

        for s in strs:
            r.append(str(len(s)))
            r.append('#')
            r.append(s)

        return ''.join(r)

    def decode(self, s: str) -> List[str]:
        r = []

        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1

            l = int(s[i:j])
            r.append(s[j+1:j+l+1])
            i = j+l+1

        return r