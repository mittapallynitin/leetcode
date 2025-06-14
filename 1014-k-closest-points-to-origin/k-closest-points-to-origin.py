class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return [
            [x,y] for x, y in 
            heapq.nlargest(k, points, lambda x: -x[0]**2 -x[1]**2)
        ]
        