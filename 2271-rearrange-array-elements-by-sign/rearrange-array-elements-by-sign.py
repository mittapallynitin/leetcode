class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        for n in nums:
            if n > 0: 
                positives.append(n)
            else:
                negatives.append(n)
        result = []
        for p, n in zip(positives, negatives):
            result.append(p)
            result.append(n)
        return result

