class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0 
        prev = None
        l = 0 
        for r in range(len(nums)):
            if nums[r] == prev:
                count += 1
                if count <= 2:
                    nums[l] = nums[r]
                    l += 1
            else:
                count = 1
                prev = nums[r]
                nums[l] = nums[r]
                l += 1
        return l