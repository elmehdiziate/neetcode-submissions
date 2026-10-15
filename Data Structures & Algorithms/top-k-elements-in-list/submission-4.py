from heapq import heappop, heappush, heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = dict()
        for i in nums:
            hs[i] = hs.get(i,0)+1
        h = []
        for key, value in hs.items():
            heapq.heappush(h, (-value,key))
        i = 0
        result = []
        while i<k:
            neg_val, key = heapq.heappop(h)
            print(key)
            result.append(key)
            i+=1
        print(result)
        return result
            