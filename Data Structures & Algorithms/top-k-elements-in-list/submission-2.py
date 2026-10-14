class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = dict()
        for i in nums:
            hs[i] = hs.get(i,0)+1
        s = dict(sorted(hs.items(), key=lambda item: item[1] , reverse = True))
        i = 0
        result = []
        while i<k:
            result.append(list(s.keys())[i])
            i+=1
        return result
            