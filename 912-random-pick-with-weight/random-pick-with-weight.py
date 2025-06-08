class Solution:

    def __init__(self, w: List[int]):
        total_weight = float(sum(w))
        self.probs = []
        curr = 0
        for prob in w:
            curr += (prob/total_weight)
            self.probs.append(curr)


    def pickIndex(self) -> int:
        from random import random
        import bisect
        x = random()
        left, right = 0, len(self.probs) - 1
        while left < right:
            mid = (left + right) // 2
            if x < self.probs[mid]:
                right = mid
            else:
                left = mid + 1
        return left

        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()