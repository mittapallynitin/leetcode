class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = ["-"]*9
        coins = ["X", "O"]
        for i, mv in enumerate(moves):
            player = coins[i % 2]
            idx = mv[0]*3 + mv[1]
            grid[idx] = player
        
        wins = [
            [0, 3, 6], [1,4,7], [2,5,8], 
            [0,1,2], [3,4,5], [6,7,8], 
            [0, 4, 8], [2,4,6]
        ]
        
        for win in wins:
            i, j, k = win
            if grid[i] + grid[j] + grid[k] == "XXX":
                return "A"
            elif grid[i] + grid[j] + grid[k] == "OOO":
                return "B"
            else:
                continue
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
