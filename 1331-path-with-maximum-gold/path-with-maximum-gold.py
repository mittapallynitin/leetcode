class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dir = [[1,0], [-1, 0], [0, 1], [0, -1]]
        # Returns gold from exploring row and col 
        def backtrack(row, col) -> int:
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0

            if grid[row][col] == 0:
                return 0

            current_gold = grid[row][col]
            grid[row][col] = 0 
            neighbor_gold = []
            for dr, dc in dir:
                r = row + dr
                c = col + dc 
                neighbor_gold.append(backtrack(r, c))
            grid[row][col] = current_gold
            return grid[row][col] + max(neighbor_gold)

        result = 0

        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, backtrack(r, c))
        return result


        