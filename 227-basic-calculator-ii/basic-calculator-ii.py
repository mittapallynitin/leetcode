class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        s = s.replace(" ", "")
        stack = deque()
        i = 0
        op = "+"
        num = 0
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
                    top = stack.pop()
                    stack.append(top*num)
                elif op == "/":
                    top = stack.pop()
                    val = int(top / num)
                    stack.append(val)
                op = char
                num = 0
            i += 1
        return sum(stack)       
        