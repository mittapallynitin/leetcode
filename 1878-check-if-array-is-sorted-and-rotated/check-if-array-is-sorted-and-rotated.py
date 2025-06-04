class Solution:
    def check(self, nums: List[int]) -> bool:
        lb, ub = float("-inf"), float("inf")
        change = 0

        for n in nums:
            if lb <= n <= ub:
                lb = n
            else:
                change += 1
                if n <= nums[0]:
                    lb = n
                    ub = nums[0]
                else:
                    return False
        return change < 2
        