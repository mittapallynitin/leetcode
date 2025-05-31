class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[r], height[l])
            max_water = max(max_water, area)

            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return max_water