class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx-1]:
                nums[ptr] = nums[idx]
                ptr += 1 
        return ptr
