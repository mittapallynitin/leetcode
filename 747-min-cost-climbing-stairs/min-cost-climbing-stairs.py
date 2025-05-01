class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        steps = [0]*(n+1)
        steps[1] = cost[0]
        for i in range(2, n+1):
            steps[i] = min(steps[i-1], steps[i-2]) + cost[i-1]
        
        return steps[n]

