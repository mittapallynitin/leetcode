class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def explore(r, c):
            if (r,c) not in visited and grid[r][c] == '1':
                visited.add((r,c))
                for lat, log in directions:
                    row = r + lat
                    col = c + log
                    if -1 < row < ROWS and -1 < col < COLS:
                        explore(row, col)
            else:
                return 
        
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    explore(r, c)
                    islands += 1
        
        return islands
        