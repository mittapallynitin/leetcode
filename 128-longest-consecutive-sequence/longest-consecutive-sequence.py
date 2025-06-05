class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        available = set(nums)
        longest = 0
        l = 0 

        for n in available:
            val = n
            if val - 1 not in available:
                curr = 1
                while val + 1 in available:
                    val += 1
                    curr += 1
                longest = max(curr, longest)
            else:
                continue
        return longest
