class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def get_next(n):
            new = 0
            for i in str(n):
                new += int(i)**2
            return new
        
        while n not in visited:
            visited.add(n)
            n = get_next(n)
            if n == 1:
                return True
        return False

        