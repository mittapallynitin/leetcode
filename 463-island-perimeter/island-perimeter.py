class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [
           [-1, 0], [1, 0],
           [0, 1], [0, -1]
        ]
        ROWS = len(grid)
        COLS = len(grid[0])

        def getPeri(r, c):
            p = 0
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0<= nr < ROWS and 0 <= nc < COLS:
                    if grid[nr][nc] == 0:
                        p += 1
                else:
                    p += 1
            return p
        res = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += getPeri(r, c)
        return res