class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        if strs:
            char = chr(127)
            for s in strs:
                r = r + s
                r = r + char
            r = r[:-1]
        else:
            r = chr(126)
        return r
        

    def decode(self, s: str) -> List[str]:
        if s == chr(126):
            return []
        char = chr(127)
        l = s.split(char)
        return l
