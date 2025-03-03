class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1, s2 = str1, str2
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        if s1[:len(s2)] != s2:
            return ""

        s1 = s1[len(s2):]
        if s1 == "":
            return s2
        
        return self.gcdOfStrings(s1, s2)


        