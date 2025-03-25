class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def interleave(i, j, k) -> bool:
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            
            if (i,j) in memo:
                return memo[(i,j)]
            

            if i < len(s1) and s1[i] == s3[k]:
                if interleave(i+1, j, k+1):
                    memo[(i, j)] = True
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if interleave(i, j+1, k+1):
                    memo[(i,j)] = True
                    return True
            
            memo[(i, j)] = False
            return False
        
        return interleave(0, 0, 0)
        