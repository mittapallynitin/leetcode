class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = None 
        i = 0 
        for r in range(len(nums)):
            if nums[r] != val:
                nums[i] = nums[r]
                val = nums[i]
                i += 1
        return i
        