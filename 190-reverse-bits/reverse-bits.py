class Solution:
    def reverseBits(self, n: int) -> int:
        s = []
        for i in range(32):
            s.append(str(n & 1))
            n = n >> 1
        return int("".join(s), 2)
        
        