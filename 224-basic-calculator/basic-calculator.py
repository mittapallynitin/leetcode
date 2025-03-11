class Solution:
    def calculate(self, s: str) -> int:

        def calculate(st):
            value = 0
            sign = 1
            i = 0
            while i < len(st):
                if st[i] == "+":
                    sign = 1
                    i += 1
                elif st[i] == "-":
                    sign = -1
                    i += 1
                else:
                    num = ""
                    while i < len(st) and st[i].isdigit():
                        num += st[i]
                        i += 1
                    value += sign * int(num)
            return value  

        stack = []
        s = s.replace(" ", "")
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                c = stack.pop()
                sign = 1
                st = ""
                while c != "(":
                    st = c + st
                    c = stack.pop()
                val = calculate(st)
                if val < 0:
                    if stack and stack[-1] == "-": 
                        stack[-1] = "+"
                        stack.append(str(abs(val)))
                    else:
                        stack.append(str(val))
                else: 
                    stack.append(str(val))
            else:
                stack.append(ch)
        return calculate("".join(stack))

