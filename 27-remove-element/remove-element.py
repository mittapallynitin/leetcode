class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[i] = nums[r]
                i += 1
        return i

        