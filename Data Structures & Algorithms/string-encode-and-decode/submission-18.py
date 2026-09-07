class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0

        while j < len(s):
            if s[j] == '#':
                size = int(s[i:j])
                res.append(s[j+1:j+size+1])
                i = j = j + size + 1
            else:
                j += 1

        return res