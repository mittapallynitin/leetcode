class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        curr = 0 
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > curr:
                ans.append(i)
                curr = max(curr, heights[i])
        
        return ans[::-1]