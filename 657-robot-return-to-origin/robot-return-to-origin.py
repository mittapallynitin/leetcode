class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vert, horz = 0, 0 
        for d in moves:
            if d == "U":
                vert += 1
            elif d == "D":
                vert -= 1
            elif d == "L":
                horz -= 1
            else:
                horz += 1
        return vert == 0 and horz == 0