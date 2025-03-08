class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M")
        ]
        ans = ""
        for div, roman in romans[::-1]:
            q = num // div
            ans += roman*q
            num = num % div
        return ans

        