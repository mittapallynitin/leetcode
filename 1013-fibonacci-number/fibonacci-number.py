class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1:
            return 1
        x1, x2 = 0, 1
        for i in range(2, n+1):
            res = x2 + x1
            x2, x1 = res, x2
        
        return x2