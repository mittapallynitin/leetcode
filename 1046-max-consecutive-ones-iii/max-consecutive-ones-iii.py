class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        count = 0 
        res = 0
        tracker = 0 
        for r in range(len(nums)):
            if nums[r] == 0:
                tracker += 1
            
            while tracker > k:
                if nums[l] == 0:
                    tracker -= 1
                count -= 1
                l += 1
            count += 1
            res = max(count, res)
        return res