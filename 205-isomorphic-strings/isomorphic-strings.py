class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(set(s)) != len(set(t)): return False

        mapST = dict()

        for i in range(len(s)):
            if s[i] not in mapST:
                mapST[s[i]] = t[i]
            elif mapST[s[i]] != t[i]:
                return False
        return True


                
            
