class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(t)
        l2 = 0 
        f = len(s)

        for r in range(n):
            if t[r] == s[l2]:
                l2 += 1
            if l2 == f:
                return True
        return False