class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = ""
        for i, j in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            i, j = int(i), int(j)
            pos = (i + j + carry) % 10
            carry = (i + j + carry) // 10
            res += str(pos)
        res += str(carry) if carry else ""
        return res[::-1]
