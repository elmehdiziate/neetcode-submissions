class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return not (len(nums) == len(temp)) 

        # temp = set()
        # for n in nums:
        #     if n in temp:
        #         return True
        #     temp.add(n)
        # return False
        