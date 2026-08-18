SEP = "<<sep>>"
EMPTY = "<<empt>>"
    
class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if strs == [""]:
            return EMPTY
        return SEP.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == EMPTY:
            return [""]
        return s.split(SEP)
