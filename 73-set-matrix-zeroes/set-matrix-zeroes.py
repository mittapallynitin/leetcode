class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        first_row_zero = any(
            [True if matrix[0][i] == 0 else False for i in range(COLS)]
        )
        first_col_zero = any(
            [
                True if matrix[i][0] == 0 else False
                for i in range(ROWS) 
            ]
        )
        
        for r in range(1, ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 
                    matrix[0][c] = 0 
        
        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(ROWS):
                    matrix[r][c] = 0
        
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                for c in range(COLS):
                    matrix[r][c] = 0
        
        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
        