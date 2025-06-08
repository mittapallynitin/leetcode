class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        if grid[0][0] or grid[-1][-1]:
            return -1

        q = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        N = len(grid)
        dirs = [
            [-1, 1], [0, 1], [1, 1],
            [-1, 0],         [1, 0],
            [-1, -1], [0, -1], [1, -1]
        ]

        while q:
            x, y, dist = q.popleft()

            if x == N-1 and y == N -1:
                return dist
            
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy

                if min(nx, ny) >= 0 and max(nx, ny) < N and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    q.append((nx, ny, dist+1))
                    visited.add((nx, ny))
        
        return -1
             

        