class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diag_sum = 0
        for i in range(n):
            diag_sum += (mat[i][i] + mat[n-1-i][i])
        
        # If odd remove the duplicate
        if n % 2 == 1:
            i = n // 2
            diag_sum -= mat[i][i]

        return diag_sum 

        