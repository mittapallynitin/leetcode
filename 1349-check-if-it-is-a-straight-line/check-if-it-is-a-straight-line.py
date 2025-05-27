class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        def f(x,y):
            LHS = (x - coordinates[0][0]) * (y - coordinates[1][1]) 
            RHS = (x - coordinates[1][0]) * (y - coordinates[0][1]) 
            return  LHS == RHS
        
        return all(f(x, y) for x, y in coordinates[2:])
        