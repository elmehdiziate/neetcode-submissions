class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)
        result = 1
        for n in nums:
            max_n = 0
            if (n-1 not in nums):
                while (n in nums):
                    max_n += 1
                    n +=1
                if max_n > result:
                    result =  max_n
        return result
            


        