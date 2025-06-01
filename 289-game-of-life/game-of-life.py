class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def get_neighbors(r, c) -> List[int]:
            neighbors = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x = r + dx
                    y = c + dy
                    if (dx or dy) and (0 <= x < m) and (0 <= y < n):
                        neighbors.append(board[x][y] % 2)
            return neighbors

        for r in range(m):
            for c in range(n):
                alive = sum(get_neighbors(r, c))
                if board[r][c] == 1:
                    if alive in [2, 3]:
                        board[r][c] = 3
                    else:
                        board[r][c] = 1
                else:
                    if alive == 3:
                        board[r][c] = 2
        
        for r in range(m):
            for c in range(n):
                board[r][c] = board[r][c] // 2
