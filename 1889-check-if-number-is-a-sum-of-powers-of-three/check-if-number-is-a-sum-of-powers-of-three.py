class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        res = ""
        while n > 0:
            res = str(n % 3) + res
            n //= 3
        return all([ch in "10" for ch in res])
        