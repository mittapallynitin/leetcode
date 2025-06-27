class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        res = 0

        if s and s[0] == "-":
            sign = -1
            s = s[1:]
        elif s and s[0] == "+":
            s = s[1:]
        
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            if res == 0 and s[i] == '0':
                continue
            res = res*10 + int(s[i])

        res = res * sign
        res = min(max(res, -2**31), 2**31-1)
        return res
        