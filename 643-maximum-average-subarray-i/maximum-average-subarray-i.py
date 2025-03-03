class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        curr = res
        l = 0
        for r in range(k, len(nums)):
            curr += nums[r] - nums[l]
            l += 1
            res = max(res, curr)
        return res / k
        