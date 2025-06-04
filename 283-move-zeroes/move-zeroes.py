class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr += 1
        
        for i in range(ptr, n):
            nums[i] = 0 