class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def interleave(s1, s2, s3) -> bool:
            if len(s1) + len(s2) != len(s3):
                memo[(s1, s2, s3)] = False
                return False
            
            if len(s1) == len(s2) == len(s3) == 0:
                memo[(s1, s2, s3)] = True
                return True
            
            if (s1, s2, s3) in memo:
                return memo[(s1, s2, s3)]

            if s1 and s1[0] == s3[0]:
                if interleave(s1[1:], s2, s3[1:]):
                    memo[(s1, s2, s3)] = True
                    return True
            
            if s2 and s2[0] == s3[0]:
                if interleave(s1, s2[1:], s3[1:]):
                    memo[(s1, s2, s3)] = True
                    return True
            
            memo[(s1, s2, s3)] = False
            return False
        
        return interleave(s1, s2, s3)
        