class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0 
        l = 0 
        n = len(nums)
        min_window = float("inf")
        for r in range(n):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_window = min(min_window, r-l+1)
                curr_sum -= nums[l]
                l += 1

        return min_window if min_window != float("inf") else 0
            