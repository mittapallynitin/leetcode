class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        ROWS, COLS = len(matrix), len(matrix[0])
        VISITED = 101

        # Inital Movement: Increment column wise
        dr = 0; dc = 1
        switch_map = {
            (1,0): (0, 1), # Switch moving right to moving bottom. 
            (0,1): (-1, 0), # Bottom -> left
            (-1,0): (0, -1), # Left -> Top 
            (0, -1): (1, 0) # Top -> Right
        }
        r, c = 0, 0


        for _ in range(ROWS*COLS):        
            output.append(matrix[r][c])
            matrix[r][c] = VISITED
            nr = r + dr
            nc = c + dc
            # switch direction
            if (nr == ROWS) or (nc == COLS) or matrix[nr][nc] == VISITED:
                dc, dr = switch_map[(dc, dr)]
                nr = r + dr
                nc = c + dc
            
            r, c = nr, nc
        
        return output