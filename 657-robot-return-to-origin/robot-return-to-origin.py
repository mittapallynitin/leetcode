class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir = {
            "R": (1, 0), 
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }

        x, y = 0, 0

        for d in moves:
            dx, dy = dir[d]
            x += dx
            y += dy
        
        return x == 0 and y == 0