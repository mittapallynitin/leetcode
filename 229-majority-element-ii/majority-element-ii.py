class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        threshold = len(nums) / 3.0   
        return [i for i, v in counts.items() if v > threshold]
