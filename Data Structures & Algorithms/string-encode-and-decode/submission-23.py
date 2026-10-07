class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        l = r = 0
        res = []
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                string = s[r+1:r+1+length]
                res.append(string)
                l = r = r+1+length
            else:
                r += 1
        return res