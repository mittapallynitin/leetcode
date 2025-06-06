class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        ans = []
        previous = []
        for i, ch in enumerate(s):
            if ch == "(":
                count += 1
                previous.append(i)
            elif ch == ")":
                count -= 1
            
            if count < 0:
                count = 0
                ans.append("-")
            else:
                ans.append(ch)
            
        if count > 0:
            for i in previous[-count:]:
                ans[i] = "-"
        
        return "".join(ch for ch in ans if ch != "-")
        