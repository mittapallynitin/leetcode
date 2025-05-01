class Solution:
    def tribonacci(self, n: int) -> int:
        x0, x1, x2 = 0, 1, 1

        if n == 0: return x0
        if n < 3: return x2

        for i in range(3, n+1):
            res = x2 + x1 + x0
            x2, x1, x0 = res, x2, x1
        return x2