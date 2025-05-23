class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            current = nums[i] > nums[i-1]
            if prev is not None and prev != current:
                return False
            prev = current
        return True
        