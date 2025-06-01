class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0 
        l, r = 0, len(nums)
        window = float("inf")
        for i in range(r):
            curr += nums[i]

            while curr >= target:
                window = min(window, i - l + 1)
                curr -= nums[l]
                l += 1 
        return window if window != float("inf") else 0

      