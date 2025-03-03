class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0
        max_len = 0 
        tracker = 0 
        for r in range(len(nums)):
            if nums[r] == 0:
                tracker += 1
            while tracker > 1:
                if nums[l] == 0:
                    tracker -= 1
                l += 1
            window = r - l
            max_len = max(max_len, window)
        return max_len
        