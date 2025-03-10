class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        prev = float("-inf")
        i = 0
        while i < len(nums):
            start = nums[i]
            end = nums[i]
            curr = nums[i]
            while i+1 < len(nums) and curr + 1 == nums[i+1]:
                i += 1
                end = curr = nums[i]
            if end != start:
                output.append(f"{start}->{end}")
            else:
                output.append(str(start))
            i += 1
        return output

        