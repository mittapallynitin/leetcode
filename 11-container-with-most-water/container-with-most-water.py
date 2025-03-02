class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0 
        l, r = 0, len(height)-1

        while l < r:
            vol = (r - l) * min(height[l], height[r])
            max_vol = max(vol, max_vol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol
        