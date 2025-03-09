class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0 
        while l < r:
            newArea = (r-l)*min(height[l], height[r])
            area = max(area, newArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area 