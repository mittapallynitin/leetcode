class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # visited = dict()
        # count = 0
        # for n in nums:
        #     if k - n in visited:
        #         count += 1
        #         visited[k-n] -= 1
        #         if visited[k-n] == 0:
        #             del visited[k-n]
        #         continue

        #     visited[n] = visited.get(n, 0) + 1
        # return count

        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            val = k - nums[l] - nums[r]
            if val == 0:
                count += 1
                l += 1
                r -= 1
            elif val > 0:
                l += 1
            else: 
                r -= 1
        return count
        