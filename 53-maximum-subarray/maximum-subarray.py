class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        l, size = 0, len(nums)
        curr = 0
        for r in range(size):
            curr += nums[r]
            ans = max(curr, ans)

            if curr < 0:
                curr = 0 
                l = r + 1
        return ans
