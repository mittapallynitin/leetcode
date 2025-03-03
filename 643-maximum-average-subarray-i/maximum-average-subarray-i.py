class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = curr = sum(nums[:k])
        for r in range(k, len(nums)):
            curr += nums[r] - nums[r -k]
            res = max(res, curr)
        return res / k
        