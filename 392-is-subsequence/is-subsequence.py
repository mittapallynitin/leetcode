class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        l = 0 
        for ch in t:
            if ch == s[l]:
                l += 1
            
            if l == len(s):
                return True
        return False
