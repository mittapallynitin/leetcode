class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_elements = len(nums)
        prefix = [1]*total_elements
        postfix = [1]*total_elements

        prev = 1
        for i in range(1, total_elements):
            prefix[i] = prev = prev*nums[i-1]
        
        prev = 1
        for i in range(total_elements-2, -1, -1):
            postfix[i] = prev = prev*nums[i+1]

        result = [0]*total_elements
        for i in range(total_elements):
            result[i] = prefix[i] * postfix[i]
        
        return result

