class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)

        rob = [0]*(n+1)
        rob[0] = 0
        rob[1] = nums[0]

        for i in range(2, n+1):
            rob[i] = max(
                nums[i-1] + rob[i-2], # rob current house + robbed amount to previous house
                rob[i-1] # skip current house
            )
        return rob[n]