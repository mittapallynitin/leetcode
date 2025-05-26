class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        zrow, zcol = set(), set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zrow.add(r)
                    zcol.add(c)
        
        for r in zrow:
            for c in range(COLS):
                matrix[r][c] = 0
        
        for c in zcol:
            for r in range(ROWS):
                matrix[r][c] = 0

        