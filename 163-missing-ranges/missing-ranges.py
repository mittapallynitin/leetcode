class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []

        for num in nums + [upper +1]:
            if num > lower:
                result.append([lower, num-1])
            lower = num + 1
        return result