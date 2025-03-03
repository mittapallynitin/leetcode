class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        l = 0 
        curr = 0 
        for r in range(len(nums)):
            curr += nums[r]
            if r - l + 1 == k:
                res = max(res, curr)
            if r - l + 1 > k:
                curr -= nums[l]
                res = max(res, curr)
                l += 1
        return res / float(k)
        