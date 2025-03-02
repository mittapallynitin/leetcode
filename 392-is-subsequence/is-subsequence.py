class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l2 = 0 
        for r in range(len(t)):
            if t[r] == s[l2]:
                l2 += 1
            if l2 == len(s):
                return True
        return False