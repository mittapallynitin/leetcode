class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 1

        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                negatives *= -1
        
        return negatives