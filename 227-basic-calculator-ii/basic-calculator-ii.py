class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        op = "+"
        num = 0
        s = s.replace(" ", "")
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = num*10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack[-1] *= num
                elif op == "/":
                    stack[-1] = int(stack[-1] / num)
                op = char
                num = 0
            i += 1
        return sum(stack)       
        