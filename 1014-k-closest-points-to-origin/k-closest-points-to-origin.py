class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.append(-point[0]**2 -point[1]**2)
        return [[x,y] for x, y, dist in heapq.nlargest(k, points, lambda x: x[2])]
        