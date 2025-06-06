class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = int(str(abs(x))[::-1])

        if -2**31 -1 <= x <= 2**31-1:
            return sign*x
        return 0