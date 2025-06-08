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
        x = random()
        for i, prob in enumerate(self.probs):
            if x < prob:
                return i

        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()