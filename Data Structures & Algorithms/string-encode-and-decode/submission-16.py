class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []
        for s in strs:
            encoding.append(str(len(s)))
            encoding.append('#')
            encoding.append(s)
        return ''.join(encoding)

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0

        while j < len(s):
            if s[j] == '#':
                l = int(s[i:j])
                res.append(s[j+1:j+1+l])
                i = j+1+l
                j = i
            else:
                j += 1
        return res