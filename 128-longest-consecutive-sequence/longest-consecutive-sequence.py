class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        available = set(nums)
        longest = 0
        for num in available:
            curr = num
            seq = 0
            if curr-1 not in available:
                while curr in available:
                    curr += 1
                    seq += 1
                longest = max(longest, seq)
        return longest


