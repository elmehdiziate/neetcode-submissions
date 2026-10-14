class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs  = dict()
        i = 0 
        result = []
        while i < len(nums):
            diff = target - nums[i]
            
            r = hs.get(diff)
            print(r)
            if r is not None:
               
                result = [r,i]
                break
            hs[nums[i]] = i
            i = i + 1
        return result
            