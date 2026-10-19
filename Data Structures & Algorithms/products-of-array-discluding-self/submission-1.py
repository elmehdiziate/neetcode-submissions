class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        prefix = lenght*[1]
        suffix = lenght*[1]
        number = 1
        result = []
        for i in range(lenght):
            prefix[i] = prefix[i]*number
            number = number* nums[i]
        number = 1
        for i in range(lenght-1, -1, -1):
            suffix[i] = suffix[i]*number
            number = number*nums[i]
        for i in range(lenght):
            result.append(suffix[i]*prefix[i])   
        return result
            


