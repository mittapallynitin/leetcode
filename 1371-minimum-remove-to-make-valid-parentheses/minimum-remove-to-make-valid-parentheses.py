class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
            else:
                continue

        to_remove = to_remove.union(set(stack))

        ans = []
        for i, ch in enumerate(s):
            if i not in to_remove:
                ans.append(ch)
        return "".join(ans)

                
        
        