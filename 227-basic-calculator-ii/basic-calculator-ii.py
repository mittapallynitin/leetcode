class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        s = s.replace(" ", "")
        stack = deque()
        i = 0
        def get_number(i):
            result = ""
            while i < len(s) and s[i].isdigit():
                result += s[i]
                i += 1
            return int(result), i

        while i < len(s):
            if s[i] in "+-":
                stack.append(s[i])
                i += 1
            elif s[i] in "*/":
                op = s[i]
                op1 = stack.pop()
                op2, i = get_number(i+1) 
                if op == "/":
                    stack.append(op1//op2)
                else:
                    stack.append(op1*op2)
            else:
                op, i = get_number(i)
                stack.append(op)
        
        curr = 0 
        sign = 1
        for op in stack:
            if op == "-":
                sign = -1
            elif isinstance(op, int):
                curr += sign * op
                sign = 1
        return curr
                
        