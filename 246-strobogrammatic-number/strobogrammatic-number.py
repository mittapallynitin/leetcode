class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        flip = {
            '1':'1',
            '6': '9',
            '9': '6',
            '8': '8',
            '0': '0'
        }

        n1 = ""
        for n in num[::-1]:
            n1 += flip.get(n, "-")
        return n1 == num