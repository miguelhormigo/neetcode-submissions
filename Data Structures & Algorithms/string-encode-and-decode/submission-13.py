class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if strs == [""]:
            return "0#"

        res = []
        for word in strs:
            res.append(f'{len(word)}#{word}')
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == "0#":
            return [""]
        
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            w_len = int(s[i:j])
            i = j + 1

            res.append(s[i:i+w_len])
            i += w_len

        return res