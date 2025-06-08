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
        # Binary Search
        return bisect.bisect_left(self.probs, x)

        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()