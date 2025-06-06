class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1 
            x = -x
        
        res = 0 

        while x:
            res = res*10 + (x % 10)
            x = x // 10
        
        if -2**31-1 <= res <= 2**31-1:
            return sign * res
        return 0