class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = dict()
        for s in strs:
            r  = dict()
            for c in s:
                r[c] = r.get(c,0)+1
            r = frozenset(r.items())
            hs.setdefault(r,[]).append(s)
        result = []
        for l in hs.values():
            result.append(l)
        return result
