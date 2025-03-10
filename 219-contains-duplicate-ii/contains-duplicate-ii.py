class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        for i, num in enumerate(nums):
            if num in visited:
                return True
            visited.add(num)
            if i - k >=0:
                visited.remove(nums[i-k])
            
        return False
        