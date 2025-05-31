class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i = 0 
        result = []
        while i < n:
            target = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1
            i += 1
            while i > 0  and i < n and nums[i] == nums[i-1]:
                i += 1
        
        return result

