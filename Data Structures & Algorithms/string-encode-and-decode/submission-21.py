class Solution:

    def encode(self, strs: List[str]) -> str:
        r = []
        for s in strs:
            r.append(f'{len(s)}#{s}')
        return ''.join(r)

    def decode(self, s: str) -> List[str]:
        l = r = 0
        sol = []

        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])

                sol.append(s[r+1:r+1+length])

                l = r = r + 1 + length

            r += 1
        
        return sol