class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = []
        for i, j in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            total = int(i) + int(j) + carry
            pos = total % 10
            carry = total // 10
            res.append(str(pos))
        if carry:
            res.append(str(carry))
        return "".join(reversed(res))
